# PiMac 2040 - Macintosh 128K/208K on RP2040-Zero
# Dual Video Engine (Composite CVBS & VGA Monitor), MicroSD SPI & Dual USB
# Developed and Engineered by SCHUBIGER.CL - https://schubiger.cl
#
# MIT License
#
cmake_minimum_required(VERSION 3.13)

# Configuration options:
option(BOARD_RP2040_ZERO "Target Waveshare / AliExpress RP2040-Zero board" ON)
set(MEMSIZE 208 CACHE STRING "Macintosh Memory size in KB (default 208K)")

# Video Mode Selector Pin (GP0 with internal pull-up)
# Open = Composite (CVBS 480i on GP8/GP9), GND = VGA (640x480 on GP26..GP29)
set(VIDEO_MODE_PIN 0 CACHE STRING "Video Mode Select GPIO Pin (default GP0)")

# Optional SD Card SPI pinouts (Default GP2=SCK, GP3=TX, GP4=RX, GP5=CS)
option(USE_SD "Build in SD support" ON)
set(SD_TX 3 CACHE STRING "SD SPI TX pin")
set(SD_RX 4 CACHE STRING "SD SPI RX pin")
set(SD_SCK 2 CACHE STRING "SD SPI SCK pin")
set(SD_CS 5 CACHE STRING "SD SPI CS pin")
set(SD_MHZ 10 CACHE STRING "SD SPI speed in MHz")

# initialize the SDK based on PICO_SDK_PATH
include(pico_sdk_import.cmake)

project(firmware)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

# For TUSB host stuff:
set(FAMILY rp2040)
set(BOARD raspberry_pi_pico)

set(TINYUSB_PATH ${PICO_SDK_PATH}/lib/tinyusb)

# umac subproject (and Musashi sub-subproject)
set(UMAC_PATH ${CMAKE_CURRENT_SOURCE_DIR}/external/umac)
set(UMAC_MUSASHI_PATH ${UMAC_PATH}/external/Musashi)
set(UMAC_INCLUDE_PATHS ${UMAC_PATH}/include ${UMAC_MUSASHI_PATH})

set(UMAC_SOURCES
  ${UMAC_PATH}/src/disc.c
  ${UMAC_PATH}/src/main.c
  ${UMAC_PATH}/src/rom.c
  ${UMAC_PATH}/src/scc.c
  ${UMAC_PATH}/src/via.c
  ${UMAC_MUSASHI_PATH}/m68kcpu.c
  ${UMAC_MUSASHI_PATH}/m68kdasm.c
  ${UMAC_MUSASHI_PATH}/m68kops.c
  ${UMAC_MUSASHI_PATH}/softfloat/softfloat.c
  )

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3 -DPICO -DMUSASHI_CNF=\\\"../include/m68kconf.h\\\" -DUMAC_MEMSIZE=${MEMSIZE}")

if (BOARD_RP2040_ZERO)
   add_compile_definitions(BOARD_RP2040_ZERO=1)
endif()

if (USE_SD)
   add_compile_definitions(USE_SD=1)
   set(FF_DISABLE_RTC ${PICO_RP2350})  # RP2350 doesn't have RTC, so disable it
   add_subdirectory(external/no-OS-FatFS-SD-SPI-RPi-Pico/FatFs_SPI build)
   set(EXTRA_SD_SRC src/sd_hw_config.c)
   set(EXTRA_SD_LIB FatFs_SPI)
   add_compile_definitions(SD_TX=${SD_TX} SD_RX=${SD_RX} SD_SCK=${SD_SCK} SD_CS=${SD_CS} SD_MHZ=${SD_MHZ})
endif()

# PiMac 2040 Native Macintosh 512x342 resolution centered in 480i NTSC / 640x480 VGA
add_compile_definitions(DISP_WIDTH=512)
add_compile_definitions(DISP_HEIGHT=342)

if (TARGET tinyusb_device)
  add_executable(firmware
    src/main.c
    src/mac_status.c
    src/video_composite.c
    src/video.c
    src/video_manager.c
    src/kbd.c
    src/hid.c
    ${EXTRA_SD_SRC}

    ${UMAC_SOURCES}
    )

  if (NOT EXISTS ${UMAC_MUSASHI_PATH}/m68kops.c)
    add_custom_command(OUTPUT ${UMAC_MUSASHI_PATH}/m68kops.c
      COMMAND echo "*** Preparing umac source ***"
      COMMAND make -C ${UMAC_PATH} prepare
      )
    add_custom_target(prepare_umac
      DEPENDS ${UMAC_MUSASHI_PATH}/m68kops.c
      )
    add_dependencies(firmware prepare_umac)
  endif()

  target_link_libraries(firmware
    pico_stdlib
    pico_multicore
    tinyusb_host
    tinyusb_board
    hardware_dma
    hardware_pio
    hardware_sync
    ${EXTRA_SD_LIB}
    )

  target_include_directories(firmware PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/include
    ${TINYUSB_PATH}/hw
    ${TINYUSB_PATH}/src
    ${UMAC_INCLUDE_PATHS}
    incbin
    )

  pico_generate_pio_header(firmware ${CMAKE_CURRENT_SOURCE_DIR}/src/pio_composite.pio)
  pico_generate_pio_header(firmware ${CMAKE_CURRENT_SOURCE_DIR}/src/pio_video.pio)

  pico_enable_stdio_uart(firmware 1)

  # Needed for UF2:
  pico_add_extra_outputs(firmware)

elseif(PICO_ON_DEVICE)
   message(WARNING "not building firmware because TinyUSB submodule is not initialized in the SDK")
endif()
