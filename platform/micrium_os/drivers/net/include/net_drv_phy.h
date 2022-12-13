/***************************************************************************//**
 * @file
 * @brief Network Device Driver - Phy
 *******************************************************************************
 * # License
 * <b>Copyright 2018 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * The licensor of this software is Silicon Laboratories Inc.  Your use of this
 * software is governed by the terms of Silicon Labs Master Software License
 * Agreement (MSLA) available at
 * www.silabs.com/about-us/legal/master-software-license-agreement.
 * The software is governed by the sections of the MSLA applicable to Micrium
 * Software.
 *
 ******************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                               MODULE
 ********************************************************************************************************
 *******************************************************************************************************/

#ifndef  NET_DRV_PHY_H
#define  NET_DRV_PHY_H

#include  <net/include/net_cfg_net.h>

#ifdef  NET_IF_ETHER_MODULE_EN

#include  <net/include/net_if_ether.h>

/********************************************************************************************************
 ********************************************************************************************************
 *                                           GLOBAL VARIABLES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 *                                               PHY GENERIC
 *******************************************************************************************************/

extern const NET_PHY_API_ETHER NetPhy_API_Generic;

/********************************************************************************************************
 *                                               PHY DP83640
 *******************************************************************************************************/

extern const NET_PHY_API_ETHER NetPhy_API_DP83640;

/********************************************************************************************************
 *                                               PHY KSZ8091
 *******************************************************************************************************/

extern const NET_PHY_API_ETHER NetPhy_API_KSZ8091;

/********************************************************************************************************
 ********************************************************************************************************
 *                                               MODULE END
 ********************************************************************************************************
 *******************************************************************************************************/

#endif // NET_IF_ETHER_MODULE_EN
#endif // NET_DRV_PHY_H