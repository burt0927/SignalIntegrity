import SignalIntegrity as si

path=os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sp = si.p.SimulatorParser()
sp.AddLine('device X 4')
sp.AddLine('device P 2')
sp.AddLine('device M 2')
sp.AddLine('device \\Gamma_P 1')
sp.AddLine('device \\Gamma_M 1')
sp.AddLine('voltagesource V1 1')
sp.AddLine('voltagesource V2 1')
sp.AddLine('connect V1 1 P 1')
sp.AddLine('connect V2 1 M 1')
sp.AddLine('connect P 2 X 1')
sp.AddLine('connect M 2 X 2')
sp.AddLine('connect X 3 \\Gamma_P 1')
sp.AddLine('connect X 4 \\Gamma_M 1')
sp.AddLine('output X 3 X 4 X 1 X 2')
ss=si.sd.SimulatorSymbolic(sp.SystemDescription(),size='small')
ss.AssignSParameters('P',si.sy.SeriesZ('Z'))
ss.AssignSParameters('M',si.sy.SeriesZ('Z'))
ss.AssignSParameters('\\Gamma_P',si.sy.ShuntZ(1,'Z'))
ss.AssignSParameters('\\Gamma_M',si.sy.ShuntZ(1,'Z'))
ss.LaTeXTransferMatrix().Emit()
