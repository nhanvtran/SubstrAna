import FWCore.ParameterSet.Config as cms

process = cms.Process("PlotROCansSignificance")

process.Options = cms.PSet(

   ## Name of the tree on which perform th training                                                                                                                                
   TreeName           = cms.string("chs"),

   ## Name for ggH signal --> match what is written in the sample list file                                                                                                             
   SignalggHName      = cms.string("RSGWW1000"),

   ## Name for ggH signal --> match what is written in the sample list file                                                                                                             
   SignalqqHName      = cms.string(""),

   ## string which use tree branches to re-weight the events                                                                                                                              
   EventWeight        = cms.string(""),

   ## 0 use both ggH and qqH as signal, 1 use only ggH as signal, 2 use only qqH as signal                                                                                                
   useTypeOfSignal    = cms.uint32(0),

   ## string which is used in the TMVATraining class to define a cut to be applied on the events                                                                                         
   PreselectionCutType = cms.string("basicJetsCutCSA14"),

   ## luminosity in order to  compute signal and bk expectations
   Lumi   = cms.double(19297),

   ## Lepton Type: Muon, Electron ,EleMu and Jets (fully hadronic)                                                                                                                        
   LeptonType         = cms.string("Jets"),

   ## output directory for root and weight file                                                                                                                                           
   outputPlotDirectory  = cms.string("TMVATrainingPlots_CHS_highPT_inclusive/"),

   ##input file and variables   
   InputInformationParam =  cms.VPSet(
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=0.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta05")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=1.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta10")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=1.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta15")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=2.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta20")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=2.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta25")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_C2beta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("C_{2}(#beta=3.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("C2beta30")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=0.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta05")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=1.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta10")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=1.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta15")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=2.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta20")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=2.5}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta25")),
#    cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_D2beta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("D_{2}(#beta=3.0}"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("D2beta30")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_tau2_tau1_beta_10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("#tau_{2}/#tau_{1} #beta=1.0"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("tau2tau1beta10")),

#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=0.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta05")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=1.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta10")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=1.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta15")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=2.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta20")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=2.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta25")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF2beta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=3.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF2beta30")),

#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=0.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta05")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=1.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta10")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=1.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta15")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=2.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta20")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=2.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta25")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF3beta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{3}(#beta=3.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF3beta30")),

#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=0.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta05")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=1.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta10")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=1.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta15")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=2.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta20")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=2.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta25")),
#   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_ECF4beta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{4}(#beta=3.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("ECF4beta30")),

   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta05_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=0.5)/ECF_{3}(#beta=0.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta05")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta10_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=1.0)/ECF_{3}(#beta=1.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta10")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta15_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=1.0)/ECF_{3}(#beta=1.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta15")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta20_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=2.0)/ECF_{3}(#beta=2.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta20")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta25_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=2.5)/ECF_{3}(#beta=2.5)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta25")),
   cms.PSet( fileName = cms.string("SingleVariablesTraining_highPT_inclusive_BDTG/outputTMVATraining_highPT/TMVATrainingResult_Ratiobeta30_PTBin_475_600_PU_0_100.root"),  inputVariableOrMethodName = cms.vstring("ECF_{2}(#beta=3.0)/ECF_{3}(#beta=3.0)"), JetPtBinOfTraining = cms.vdouble(475,600), PileUpBinOfTraining = cms.vdouble(0,100), ReducedName = cms.string("Ratiobeta30")),
 

  )
)
