
# -*- coding: utf-8 -*-

from . static import Base_RM_Register
from . TXFRONT_NS_field import *


class RM_Register_TXFRONT_NS_IPVERSION(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_IPVERSION, self).__init__(rmio, label,
            0xb8048000, 0x000,
            'IPVERSION', 'TXFRONT_NS.IPVERSION', 'read-only',
            u"",
            0x00000001, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IPVERSION = RM_Field_TXFRONT_NS_IPVERSION_IPVERSION(self)
        self.zz_fdict['IPVERSION'] = self.IPVERSION
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_EN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_EN, self).__init__(rmio, label,
            0xb8048000, 0x004,
            'EN', 'TXFRONT_NS.EN', 'read-write',
            u"",
            0x00000000, 0x00000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.EN = RM_Field_TXFRONT_NS_EN_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.DISABLING = RM_Field_TXFRONT_NS_EN_DISABLING(self)
        self.zz_fdict['DISABLING'] = self.DISABLING
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_SWRST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_SWRST, self).__init__(rmio, label,
            0xb8048000, 0x008,
            'SWRST', 'TXFRONT_NS.SWRST', 'read-write',
            u"",
            0x00000000, 0x00000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.SWRST = RM_Field_TXFRONT_NS_SWRST_SWRST(self)
        self.zz_fdict['SWRST'] = self.SWRST
        self.RESETTING = RM_Field_TXFRONT_NS_SWRST_RESETTING(self)
        self.zz_fdict['RESETTING'] = self.RESETTING
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_DISCLK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_DISCLK, self).__init__(rmio, label,
            0xb8048000, 0x010,
            'DISCLK', 'TXFRONT_NS.DISCLK', 'read-write',
            u"",
            0x00000000, 0x00000001,
            0x00001000, 0x00002000,
            0x00003000)

        self.DISCLK = RM_Field_TXFRONT_NS_DISCLK_DISCLK(self)
        self.zz_fdict['DISCLK'] = self.DISCLK
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1CFG, self).__init__(rmio, label,
            0xb8048000, 0x100,
            'INT1CFG', 'TXFRONT_NS.INT1CFG', 'read-write',
            u"",
            0x000000C7, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RATIO = RM_Field_TXFRONT_NS_INT1CFG_RATIO(self)
        self.zz_fdict['RATIO'] = self.RATIO
        self.GAINSHIFT = RM_Field_TXFRONT_NS_INT1CFG_GAINSHIFT(self)
        self.zz_fdict['GAINSHIFT'] = self.GAINSHIFT
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF01(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF01, self).__init__(rmio, label,
            0xb8048000, 0x104,
            'INT1COEF01', 'TXFRONT_NS.INT1COEF01', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF0 = RM_Field_TXFRONT_NS_INT1COEF01_COEFF0(self)
        self.zz_fdict['COEFF0'] = self.COEFF0
        self.COEFF1 = RM_Field_TXFRONT_NS_INT1COEF01_COEFF1(self)
        self.zz_fdict['COEFF1'] = self.COEFF1
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF23(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF23, self).__init__(rmio, label,
            0xb8048000, 0x108,
            'INT1COEF23', 'TXFRONT_NS.INT1COEF23', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF2 = RM_Field_TXFRONT_NS_INT1COEF23_COEFF2(self)
        self.zz_fdict['COEFF2'] = self.COEFF2
        self.COEFF3 = RM_Field_TXFRONT_NS_INT1COEF23_COEFF3(self)
        self.zz_fdict['COEFF3'] = self.COEFF3
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF45(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF45, self).__init__(rmio, label,
            0xb8048000, 0x10C,
            'INT1COEF45', 'TXFRONT_NS.INT1COEF45', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF4 = RM_Field_TXFRONT_NS_INT1COEF45_COEFF4(self)
        self.zz_fdict['COEFF4'] = self.COEFF4
        self.COEFF5 = RM_Field_TXFRONT_NS_INT1COEF45_COEFF5(self)
        self.zz_fdict['COEFF5'] = self.COEFF5
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF67(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF67, self).__init__(rmio, label,
            0xb8048000, 0x110,
            'INT1COEF67', 'TXFRONT_NS.INT1COEF67', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF6 = RM_Field_TXFRONT_NS_INT1COEF67_COEFF6(self)
        self.zz_fdict['COEFF6'] = self.COEFF6
        self.COEFF7 = RM_Field_TXFRONT_NS_INT1COEF67_COEFF7(self)
        self.zz_fdict['COEFF7'] = self.COEFF7
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF89(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF89, self).__init__(rmio, label,
            0xb8048000, 0x114,
            'INT1COEF89', 'TXFRONT_NS.INT1COEF89', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF8 = RM_Field_TXFRONT_NS_INT1COEF89_COEFF8(self)
        self.zz_fdict['COEFF8'] = self.COEFF8
        self.COEFF9 = RM_Field_TXFRONT_NS_INT1COEF89_COEFF9(self)
        self.zz_fdict['COEFF9'] = self.COEFF9
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF1011(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF1011, self).__init__(rmio, label,
            0xb8048000, 0x118,
            'INT1COEF1011', 'TXFRONT_NS.INT1COEF1011', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF10 = RM_Field_TXFRONT_NS_INT1COEF1011_COEFF10(self)
        self.zz_fdict['COEFF10'] = self.COEFF10
        self.COEFF11 = RM_Field_TXFRONT_NS_INT1COEF1011_COEFF11(self)
        self.zz_fdict['COEFF11'] = self.COEFF11
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF1213(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF1213, self).__init__(rmio, label,
            0xb8048000, 0x11C,
            'INT1COEF1213', 'TXFRONT_NS.INT1COEF1213', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF12 = RM_Field_TXFRONT_NS_INT1COEF1213_COEFF12(self)
        self.zz_fdict['COEFF12'] = self.COEFF12
        self.COEFF13 = RM_Field_TXFRONT_NS_INT1COEF1213_COEFF13(self)
        self.zz_fdict['COEFF13'] = self.COEFF13
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT1COEF1415(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT1COEF1415, self).__init__(rmio, label,
            0xb8048000, 0x120,
            'INT1COEF1415', 'TXFRONT_NS.INT1COEF1415', 'read-write',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF14 = RM_Field_TXFRONT_NS_INT1COEF1415_COEFF14(self)
        self.zz_fdict['COEFF14'] = self.COEFF14
        self.COEFF15 = RM_Field_TXFRONT_NS_INT1COEF1415_COEFF15(self)
        self.zz_fdict['COEFF15'] = self.COEFF15
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_INT2CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_INT2CFG, self).__init__(rmio, label,
            0xb8048000, 0x124,
            'INT2CFG', 'TXFRONT_NS.INT2CFG', 'read-write',
            u"",
            0x00000802, 0x00007FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RATIO = RM_Field_TXFRONT_NS_INT2CFG_RATIO(self)
        self.zz_fdict['RATIO'] = self.RATIO
        self.GAINSHIFT = RM_Field_TXFRONT_NS_INT2CFG_GAINSHIFT(self)
        self.zz_fdict['GAINSHIFT'] = self.GAINSHIFT
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_SRCCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_SRCCFG, self).__init__(rmio, label,
            0xb8048000, 0x128,
            'SRCCFG', 'TXFRONT_NS.SRCCFG', 'read-write',
            u"",
            0x00000002, 0x0007FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RATIO = RM_Field_TXFRONT_NS_SRCCFG_RATIO(self)
        self.zz_fdict['RATIO'] = self.RATIO
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXIQIMB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXIQIMB, self).__init__(rmio, label,
            0xb8048000, 0x12C,
            'TXIQIMB', 'TXFRONT_NS.TXIQIMB', 'read-write',
            u"",
            0x00000000, 0x0FFF0FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.EPSILON = RM_Field_TXFRONT_NS_TXIQIMB_EPSILON(self)
        self.zz_fdict['EPSILON'] = self.EPSILON
        self.PHI = RM_Field_TXFRONT_NS_TXIQIMB_PHI(self)
        self.zz_fdict['PHI'] = self.PHI
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXDCOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXDCOFFSET, self).__init__(rmio, label,
            0xb8048000, 0x130,
            'TXDCOFFSET', 'TXFRONT_NS.TXDCOFFSET', 'read-write',
            u"",
            0x00000000, 0x03FF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DCOFFSETI = RM_Field_TXFRONT_NS_TXDCOFFSET_DCOFFSETI(self)
        self.zz_fdict['DCOFFSETI'] = self.DCOFFSETI
        self.DCOFFSETQ = RM_Field_TXFRONT_NS_TXDCOFFSET_DCOFFSETQ(self)
        self.zz_fdict['DCOFFSETQ'] = self.DCOFFSETQ
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXRAMPUP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXRAMPUP, self).__init__(rmio, label,
            0xb8048000, 0x134,
            'TXRAMPUP', 'TXFRONT_NS.TXRAMPUP', 'read-write',
            u"",
            0x00002088, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.MODE = RM_Field_TXFRONT_NS_TXRAMPUP_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.DELAY = RM_Field_TXFRONT_NS_TXRAMPUP_DELAY(self)
        self.zz_fdict['DELAY'] = self.DELAY
        self.STEP = RM_Field_TXFRONT_NS_TXRAMPUP_STEP(self)
        self.zz_fdict['STEP'] = self.STEP
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXDCRAMPUP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXDCRAMPUP, self).__init__(rmio, label,
            0xb8048000, 0x138,
            'TXDCRAMPUP', 'TXFRONT_NS.TXDCRAMPUP', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DELAY = RM_Field_TXFRONT_NS_TXDCRAMPUP_DELAY(self)
        self.zz_fdict['DELAY'] = self.DELAY
        self.DCRI = RM_Field_TXFRONT_NS_TXDCRAMPUP_DCRI(self)
        self.zz_fdict['DCRI'] = self.DCRI
        self.DCRQ = RM_Field_TXFRONT_NS_TXDCRAMPUP_DCRQ(self)
        self.zz_fdict['DCRQ'] = self.DCRQ
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXGAIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXGAIN, self).__init__(rmio, label,
            0xb8048000, 0x13C,
            'TXGAIN', 'TXFRONT_NS.TXGAIN', 'read-write',
            u"",
            0x000001FF, 0x000003FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.GAINDIG = RM_Field_TXFRONT_NS_TXGAIN_GAINDIG(self)
        self.zz_fdict['GAINDIG'] = self.GAINDIG
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXCLIP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXCLIP, self).__init__(rmio, label,
            0xb8048000, 0x140,
            'TXCLIP', 'TXFRONT_NS.TXCLIP', 'read-write',
            u"",
            0x080007FF, 0x0FFF0FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CLIPPOS = RM_Field_TXFRONT_NS_TXCLIP_CLIPPOS(self)
        self.zz_fdict['CLIPPOS'] = self.CLIPPOS
        self.CLIPNEG = RM_Field_TXFRONT_NS_TXCLIP_CLIPNEG(self)
        self.zz_fdict['CLIPNEG'] = self.CLIPNEG
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_TXPREDIST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_TXPREDIST, self).__init__(rmio, label,
            0xb8048000, 0x144,
            'TXPREDIST', 'TXFRONT_NS.TXPREDIST', 'read-write',
            u"",
            0x00000000, 0x3FFF3FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BETAAMP = RM_Field_TXFRONT_NS_TXPREDIST_BETAAMP(self)
        self.zz_fdict['BETAAMP'] = self.BETAAMP
        self.BETAPHA = RM_Field_TXFRONT_NS_TXPREDIST_BETAPHA(self)
        self.zz_fdict['BETAPHA'] = self.BETAPHA
        self.__dict__['zz_frozen'] = True


class RM_Register_TXFRONT_NS_DAC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TXFRONT_NS_DAC, self).__init__(rmio, label,
            0xb8048000, 0x150,
            'DAC', 'TXFRONT_NS.DAC', 'read-write',
            u"",
            0x00000002, 0x00000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.CONNECTTEST = RM_Field_TXFRONT_NS_DAC_CONNECTTEST(self)
        self.zz_fdict['CONNECTTEST'] = self.CONNECTTEST
        self.DACFORMAT = RM_Field_TXFRONT_NS_DAC_DACFORMAT(self)
        self.zz_fdict['DACFORMAT'] = self.DACFORMAT
        self.__dict__['zz_frozen'] = True

