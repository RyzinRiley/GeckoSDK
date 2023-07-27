/***************************************************************************//**
 * @file
 * @brief UARTDRV_EUSART Config
 *******************************************************************************
 * # License
 * <b>Copyright 2019 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * SPDX-License-Identifier: Zlib
 *
 * The licensor of this software is Silicon Laboratories Inc.
 *
 * This software is provided 'as-is', without any express or implied
 * warranty. In no event will the authors be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 *
 ******************************************************************************/

#ifndef SL_UARTDRV_EUSART_MIKROE_CONFIG_H
#define SL_UARTDRV_EUSART_MIKROE_CONFIG_H

#include "em_eusart.h"
// <<< Use Configuration Wizard in Context Menu >>>

// <h> EUSART settings
// <o SL_UARTDRV_EUSART_MIKROE_BAUDRATE> Baud rate
// <i> Default: 115200
#define SL_UARTDRV_EUSART_MIKROE_BAUDRATE        115200

// <o SL_UARTDRV_EUSART_MIKROE_LF_MODE> Low frequency mode
// <true=> True
// <false=> False
#define SL_UARTDRV_EUSART_MIKROE_LF_MODE         false

// <o SL_UARTDRV_EUSART_MIKROE_PARITY> Parity mode to use
// <eusartNoParity=> No Parity
// <eusartEvenParity=> Even parity
// <eusartOddParity=> Odd parity
// <i> Default: eusartNoParity
#define SL_UARTDRV_EUSART_MIKROE_PARITY          eusartNoParity

// <o SL_UARTDRV_EUSART_MIKROE_STOP_BITS> Number of stop bits to use.
// <eusartStopbits0p5=> 0.5 stop bits
// <eusartStopbits1=> 1 stop bits
// <eusartStopbits1p5=> 1.5 stop bits
// <eusartStopbits2=> 2 stop bits
// <i> Default: eusartStopbits1
#define SL_UARTDRV_EUSART_MIKROE_STOP_BITS       eusartStopbits1

// <o SL_UARTDRV_EUSART_MIKROE_FLOW_CONTROL_TYPE> Flow control method
// <uartdrvFlowControlNone=> None
// <uartdrvFlowControlSw=> Software XON/XOFF
// <uartdrvFlowControlHw=> nRTS/nCTS hardware handshake
// <uartdrvFlowControlHwUart=> UART peripheral controls nRTS/nCTS
// <i> Default: uartdrvFlowControlHwUart
#define SL_UARTDRV_EUSART_MIKROE_FLOW_CONTROL_TYPE uartdrvFlowControlNone

// <o SL_UARTDRV_EUSART_MIKROE_OVERSAMPLING> Oversampling selection
// <eusartOVS16=> 16x oversampling
// <eusartOVS8=> 8x oversampling
// <eusartOVS6=> 6x oversampling
// <eusartOVS4=> 4x oversampling
// <eusartOVS0=> Oversampling disabled
// <i> Default: eusartOVS16
#define SL_UARTDRV_EUSART_MIKROE_OVERSAMPLING      eusartOVS16

// <o SL_UARTDRV_EUSART_MIKROE_MVDIS> Majority vote disable for 16x, 8x and 6x oversampling modes
// <eusartMajorityVoteEnable=> False
// <eusartMajorityVoteDisable=> True
// <i> Default: eusartMajorityVoteEnable
#define SL_UARTDRV_EUSART_MIKROE_MVDIS             eusartMajorityVoteEnable

// <o SL_UARTDRV_EUSART_MIKROE_RX_BUFFER_SIZE> Size of the receive operation queue
// <i> Default: 6
#define SL_UARTDRV_EUSART_MIKROE_RX_BUFFER_SIZE  6

// <o SL_UARTDRV_EUSART_MIKROE_TX_BUFFER_SIZE> Size of the transmit operation queue
// <i> Default: 6
#define SL_UARTDRV_EUSART_MIKROE_TX_BUFFER_SIZE 6
// </h>
// <<< end of configuration section >>>

// <<< sl:start pin_tool >>>
// <eusart signal=TX,RX,(CTS),(RTS)> SL_UARTDRV_EUSART_MIKROE
// $[EUSART_SL_UARTDRV_EUSART_MIKROE]
#define SL_UARTDRV_EUSART_MIKROE_PERIPHERAL      EUSART1
#define SL_UARTDRV_EUSART_MIKROE_PERIPHERAL_NO   1

// EUSART1 TX on PA04
#define SL_UARTDRV_EUSART_MIKROE_TX_PORT         gpioPortA
#define SL_UARTDRV_EUSART_MIKROE_TX_PIN          4

// EUSART1 RX on PA05
#define SL_UARTDRV_EUSART_MIKROE_RX_PORT         gpioPortA
#define SL_UARTDRV_EUSART_MIKROE_RX_PIN          5



// [EUSART_SL_UARTDRV_EUSART_MIKROE]$
// <<< sl:end pin_tool >>>
#endif // SL_UARTDRV_EUSART_MIKROE_CONFIG_H