import SignalIntegrity as si

sdp=si.p.SystemDescriptionParser()
sdp.AddLines(['device D 2','port 1 D 1 2 D 1 3 D 2'])
ssps=si.sd.SystemSParametersSymbolic(sdp.SystemDescription())
ssps.AssignSParameters('D',si.sy.SeriesZ('Z'))
ssps.LaTeXSolution(size='big').Emit()
