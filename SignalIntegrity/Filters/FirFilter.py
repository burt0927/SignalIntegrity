from numpy import convolve



class FirFilter(object):
    def __init__(self,fd,ft):
        self.m_fd = fd
        self.m_ft=ft
    def FilterTaps(self):
        return self.m_ft
    def FilterDescriptor(self):
        return self.m_fd
    def FilterWaveform(self,wf):
        from SignalIntegrity.Waveform.Waveform import Waveform
        td = wf.TimeDescriptor().ApplyFilter(self.FilterDescriptor())
        filteredwf=convolve(wf.Values(),self.FilterTaps(),'valid').tolist()
        return Waveform(td,filteredwf)
    def Print(self):
        self.FilterDescriptor().Print()
        print str(self.FilterTaps())