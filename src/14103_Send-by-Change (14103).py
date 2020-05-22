# coding: UTF-8
##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Send_by_Change_14103_14103(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hsl20_3_sbc")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_NVAL=1
        self.PIN_I_NCHANGE=2
        self.PIN_O_NVAL=1
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    m_bInit = False
    m_nLastVal = 0

    def on_init(self):
        pass

    def on_input_value(self, index, value):

        if index == self.PIN_I_NVAL:

            bUpdate = False
            nVal = self._get_input_value(self.PIN_I_NVAL)
            nMaxDelta = self._get_input_value(self.PIN_I_NCHANGE)

            if not self.m_bInit:
                bUpdate = True
                self.m_bInit = True

            else:
                nRangeLow = self.m_nLastVal - nMaxDelta
                nRangeHi = self.m_nLastVal + nMaxDelta

                if (nVal < nRangeLow) or (nVal > nRangeHi):
                    bUpdate = True

            if bUpdate:
                    self.m_nLastVal = nVal
                    self._set_output_value(self.PIN_O_NVAL, self.m_nLastVal)
