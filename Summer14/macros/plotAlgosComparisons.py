#! /usr/bin/env python
import os
import glob
import math
import array
import sys
import time

import ROOT

ROOT.gROOT.ProcessLine(".L ~/tdrstyle.C");
ROOT.setTDRStyle();
#ROOT.gStyle.SetPadLeftMargin(0.16);
ROOT.gStyle.SetLegendFont(42)
ROOT.gStyle.SetTextFont(42)

############################################
#            Job steering                  #
############################################
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-b', action='store_true', dest='noX', default=False, help='no X11 windows')
parser.add_option('-i','--input',action="store",type="string",dest="input",default="outtre.root")
parser.add_option('-o','--outdir',action="store",type="string",dest="outdir",default="plots")
parser.add_option('--nPU',action="store",type="int",dest="nPU",default=40)
parser.add_option('-r',action="store",type="float",dest="radius",default=0.8)
parser.add_option('--minPt',action="store",type="float",dest="minPt",default=25.)
parser.add_option('--maxPt',action="store",type="float",dest="maxPt",default=300.)
parser.add_option('--minEta',action="store",type="float",dest="minEta",default=0.)
parser.add_option('--maxEta',action="store",type="float",dest="maxEta",default=2.5)

(options, args) = parser.parse_args()



# cms preliminary 
cmsprel = ROOT.TLatex(0.20,0.96,("CMS Simulation Preliminary, #sqrt{s} = 13 TeV"))
cmsprel.SetNDC()
cmsprel.SetTextSize(0.03)

# text
latex1 = ROOT.TLatex(0.20,0.90,("Anti-kT (R=%.1f)"%(options.radius)))
latex1.SetNDC()
latex1.SetTextSize(0.03)
latex2 = ROOT.TLatex(0.20,0.85,("<n_{PU}> = "+str(options.nPU)))
latex2.SetNDC()
latex2.SetTextSize(0.03)
latex3 = ROOT.TLatex(0.20,0.80,("%.0f GeV < p_{T} < %.0f GeV "%(options.minPt,options.maxPt)))
latex3.SetNDC()
latex3.SetTextSize(0.03)
latex4 = ROOT.TLatex(0.20,0.75,("%.1f  < |#eta| < %.1f "%(options.minEta,options.maxEta)))
if options.minEta == 0:
    latex4 = ROOT.TLatex(0.20,0.75,("|#eta| < %.1f "%(options.maxEta)))
latex4.SetNDC()
latex4.SetTextSize(0.03)


############################################################
def makeKinComparisonPlots(f, hname, types, plotAttributes, styles, outdir):

    # canvas
    c = ROOT.TCanvas(plotAttributes[0],plotAttributes[0],700,700);

    # legend
    leg = ROOT.TLegend(0.7,0.7,0.93,0.9);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);

    h = {}
    ymax = -1
    for typ, suff in types.iteritems():
        h[typ] = f.Get(suff+'/'+hname+'_'+suff)
        tmp = h[typ].GetMaximum()
        if tmp > ymax:
            ymax = tmp

    n = 0        
    for typ in types:
        if (h[typ]):
            leg.AddEntry(h[typ], typ, "l")
            h[typ].SetXTitle(plotAttributes[1])
            h[typ].SetYTitle(plotAttributes[2])
            h[typ].SetLineColor(styles[typ][0])
            h[typ].SetLineStyle(styles[typ][1])
            h[typ].SetLineWidth(styles[typ][2])
            h[typ].GetYaxis().SetTitleOffset(1.3)
            c.cd()
            if (n==0):
                if 'njet' in hname:
                    h[typ].GetXaxis().SetRangeUser(0,20)
                if 'pt' in hname:
                    h[typ].GetXaxis().SetRangeUser(options.minPt, options.maxPt)
                h[typ].GetYaxis().SetRangeUser(0,ymax*1.3)
                h[typ].Draw()
            else:
                h[typ].Draw('same')
            n = n + 1    


    cmsprel.Draw()
    latex1.Draw()
    latex2.Draw()
    latex3.Draw()
    latex4.Draw()
    leg.Draw()
    
    c.SaveAs(outdir+"/"+c.GetName()+".png");
    c.SaveAs(outdir+"/"+c.GetName()+".pdf");
    c.SaveAs(outdir+"/"+c.GetName()+".root");


def makeResponseComparisonPlots(f, hname, types, plotAttributes, styles, outdir):

    # canvas
    c = ROOT.TCanvas(plotAttributes[0],plotAttributes[0],700,700);

    # legend
    leg = ROOT.TLegend(0.7,0.7,0.93,0.9);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);

    h = {}
    ymax = -1
    for typ, suff in types.iteritems():
        h[typ] = f.Get(suff+'/'+hname+'_'+suff)
        tmp = h[typ].GetMaximum()
        if (tmp > ymax and typ !='GEN'):
            ymax = tmp
            
    n = 0        
    for typ in types:
        if (h[typ] and typ != 'GEN' ):
            leg.AddEntry(h[typ], typ, "l")
            h[typ].SetXTitle(plotAttributes[1])
            h[typ].SetYTitle(plotAttributes[2])
            h[typ].SetLineColor(styles[typ][0])
            h[typ].SetLineStyle(styles[typ][1])
            h[typ].SetLineWidth(styles[typ][2])
            h[typ].GetYaxis().SetTitleOffset(1.3)
            c.cd()
            if (n==0):
                h[typ].GetYaxis().SetRangeUser(0,ymax*1.3)
                h[typ].Draw()
            else:
                h[typ].Draw('same')
        n = n + 1    

    cmsprel.Draw()
    latex1.Draw()
    latex2.Draw()
    latex3.Draw()
    latex4.Draw()
    leg.Draw()
    
    c.SaveAs(outdir+"/"+c.GetName()+".png");
    c.SaveAs(outdir+"/"+c.GetName()+".pdf");
    c.SaveAs(outdir+"/"+c.GetName()+".root");


def makePileupPlots(f, typ, suff, styles, outdir):

    # legend                                                                                                                                                                
    leg = ROOT.TLegend(0.7,0.7,0.93,0.9);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);

    # text                                                                                                  
    latex4 = ROOT.TLatex(0.20,0.89,typ);
    latex4.SetNDC()
    latex4.SetTextSize(0.03)
    latex1 = ROOT.TLatex(0.20,0.84,("Anti-kT (R=%.1f)")%(options.radius));
    latex1.SetNDC()
    latex1.SetTextSize(0.03)
    latex2 = ROOT.TLatex(0.20,0.79,("n_{PU} = %d"%(options.nPU)));
    latex2.SetNDC()
    latex2.SetTextSize(0.03)
    latex3 = ROOT.TLatex(0.20,0.74,("%.0f GeV < p_{T} < %.0f GeV "%(options.minPt,options.maxPt)))
    latex3.SetNDC()
    latex3.SetTextSize(0.03)

    xtitle = {'pt':'p^{T} (GeV)', 'eta':'#eta'}
    for var in 'pt','eta':

        h     = f.Get(suff+'/h'+var+'_'+suff)
        hpu   = f.Get(suff+'/h'+var+'_pu_'+suff)
        hgood = f.Get(suff+'/h'+var+'_good_'+suff)
             
        h.SetLineColor(styles[typ][0])
        h.SetXTitle(xtitle[var])
        h.SetYTitle('events')
        col = ROOT.kGray+3
        hpu.SetLineColor(col)
        hpu.SetLineStyle(2)
        hgood.SetLineColor(col)
        hgood.SetLineStyle(1)

        if var == 'pt':
            leg.AddEntry(hgood,"Real jets","L")
            leg.AddEntry(hpu,"Pile-up","L")
            leg.AddEntry(h,"All","L")
            h.GetXaxis().SetRangeUser(options.minPt, options.maxPt)

        # canvas
        c = ROOT.TCanvas(var+'_'+typ,var+'_'+typ,700,700);

        h.GetYaxis().SetRangeUser(0,h.GetMaximum()*1.1)
        h.Draw()
        hpu.Draw("same")
        hgood.Draw("same")
        leg.Draw()
        latex1.Draw();
        latex2.Draw();
        latex3.Draw();
        latex4.Draw();

        # save plots
        for p in '.pdf', '.png', '.root':
            c.SaveAs(outdir+'/'+c.GetName()+p)


def makeRealJetFractionPlots(f, types, styles, outdir):

    # legend                                                                                                                                                                                        
    leg = ROOT.TLegend(0.7,0.7,0.93,0.9);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);
 
    # text
    latex1 = ROOT.TLatex(0.20,0.89,("Anti-kT (R=%.1f)"%(options.radius)))
    latex1.SetNDC()
    latex1.SetTextSize(0.03)
    latex2 = ROOT.TLatex(0.20,0.84,("n_{PU} = "+str(options.nPU)))
    latex2.SetNDC()
    latex2.SetTextSize(0.03)
    latex3 = ROOT.TLatex(0.20,0.79,("%.0f GeV < p_{T} < %.0f GeV "%(options.minPt,options.maxPt)))
    latex3.SetNDC()
    latex3.SetTextSize(0.03)

    for var in 'pt', 'ptraw', 'eta', 'npu':
        c = ROOT.TCanvas('realjetsfraction_'+var,'realjetsfraction_'+var,700,700);
        hgoodfraction=[]
        n = 0
        for typ,suff in types.iteritems():
            h = f.Get(suff+'/h'+var+'_'+suff)
            ROOT.gROOT.cd()
            hgoodfraction.append( (f.Get(suff+'/h'+var+'_good_'+suff)).Clone('hgoodfraction_'+var+'_'+typ) )
            hgoodfraction[n].Divide(hgoodfraction[n],h,1,1)
            hgoodfraction[n].SetLineColor(styles[typ][0])
            hgoodfraction[n].SetLineStyle(styles[typ][1])
            hgoodfraction[n].SetLineWidth(styles[typ][2])
            hgoodfraction[n].SetXTitle(var)
            hgoodfraction[n].SetYTitle("fraction of real jets")
            hgoodfraction[n].GetYaxis().SetRangeUser(0,1.5)
            if var == 'pt':
                leg.AddEntry(hgoodfraction[n], typ, "l")
                hgoodfraction[n].GetXaxis().SetRangeUser(options.minPt, options.maxPt)
            if var ==  'npu':
                hgoodfraction[n].GetXaxis().SetRangeUser(20,70)
            if (n == 0):
                hgoodfraction[n].Draw()
            else:
                hgoodfraction[n].Draw('same')
            n = n + 1 
   
        c.cd()
        latex1.Draw()
        latex2.Draw()
        latex3.Draw()
        leg.Draw()
    
        # save plots
        for p in '.pdf', '.png', '.root':
            c.SaveAs(outdir+'/'+c.GetName()+p)    


def makeEfficiencyPlots(f, types, styles, outdir):
    
    # legend                                               
    leg = ROOT.TLegend(0.7,0.7,0.93,0.9);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);

    for var in 'ptgen', 'eta', 'npu':
        c = ROOT.TCanvas('efficiency_'+var,'efficiency_'+var,700,700);
        ROOT.gROOT.cd()
        hden = f.Get(('gen/h'+var+'_gen').replace('hptgen','hpt')).Clone('hden')
        hnum = []
        n = 0
        for typ,suff in types.iteritems():
            hnum.append( f.Get(suff+'/h'+var+'_good_'+suff))
            hnum[n].Divide(hnum[n], hden, 1., 1.)
            hnum[n].SetLineColor(styles[typ][0])
            hnum[n].SetLineStyle(styles[typ][1])
            hnum[n].SetLineWidth(styles[typ][2])
            hnum[n].GetXaxis().SetTitle(var)
            hnum[n].GetYaxis().SetTitle("efficiency")
            hnum[n].GetYaxis().SetRangeUser(0,1.5)
            if (var == 'ptgen'):
                leg.AddEntry(hnum[n], typ, "l")
                hnum[n].GetXaxis().SetRangeUser(options.minPt,options.maxPt)
            if var ==  'npu':
                hnum[n].GetXaxis().SetRangeUser(20,70)
            if (n == 0):
                hnum[n].Draw()
            else:
                hnum[n].Draw('same')
            n = n + 1 
               
        c.cd()
        cmsprel.Draw()
        latex1.Draw()
        latex2.Draw()
        latex3.Draw()
        latex4.Draw()
        leg.Draw()
    
        # save plots
        for p in '.pdf', '.png', '.root':
            c.SaveAs(outdir+'/'+c.GetName()+p)    



if __name__ == '__main__':

    filename = options.input
    outdir   = options.outdir
    try:
        os.mkdir(outdir)
    except:
        print 'Cannot create output directory: directory already exists'
        sys.exit()

    docmssw = False
    #docmssw = True
    
    types = {'GEN':'gen','PUPPI':'puppi','PF':'pf','PF+CHS':'pfchs'}
    if (docmssw):
        types = {'GEN':'gen','PUPPI':'puppi','PF':'pf','PF+CHS':'pfchs','PF-CMSSW':'pfcmssw'}

    histograms = {'hnjets'         : ['njets','N_{jets}','events',1], # hname:name,x-title,y-title,rebin

                  'hnparticles'    : ['nparticles','N_{particles}','events',1] ,
                  'hnneutrals'     : ['nneutrals','N_{neutrals}','events',1] ,
                  'hncharged'      : ['ncharged','N_{charged}','events',1] ,

                  'hptraw'         : ['ptraw','p_{T,raw} (GeV)','events',5], 
                  'hpt'            : ['pt','p_{T} (GeV)','events',5],
                  'hptcorr'        : ['ptcorr','p_{T} (GeV)','events',5],

                  'heta'           : ['eta','#eta','events',2],

                  'hmraw'          : ['mraw','m_{raw} (GeV)','events',1],
                  'hm'             : ['m','m (GeV)','events',1],
                  'hmtrim'         : ['mtrim','m_{trim} (GeV)','events',1],
                  'hmtrimsafe'     : ['mtrimsafe','m_{trim} (GeV)','events',1],
                  'hmclean'        : ['mclean','m (GeV)','events',1],
                  'hmconst'        : ['mconst','m (GeV)','events',1],

                  'hptraw_response' : ['ptraw_response','p_{T,raw} - p_{T,gen}(GeV)','events',1], 
                  'hpt_response'    : ['pt_response','p_{T} - p_{T,gen}(GeV)','events',1],
                  'hptcorr_response': ['ptcorr_response','p_{T} - p_{T,gen}(GeV)','events',1],

                  'hmraw_response'  : ['mraw_response','m_{raw} - m_{gen}(GeV)','events',1],
                  'hm_response'     : ['m_response','m - m_{gen}(GeV)','events',1],
                  'hmtrim_response' : ['mtrim_response','m_{trim} - m_{gen}(GeV)','events',1],
                  'hmtrimsafe_response' : ['mtrimsafe_response','m_{trim} - m_{gen}(GeV)','events',1],
                  'hmclean_response' : ['mclean_response','m - m_{gen}(GeV)','events',1],
                  'hmconst_response' : ['mconst_response','m - m_{gen}(GeV)','events',1],

                  'htau21_leadjet':['tau21_leadjet','#tau_{2}/#tau_{1}','events',10],
                  'htau21_softdrop_leadjet':['tau21_softdrop_leadjet','#tau_{2}/#tau_{1}','events',10],

                  # lead jet
                  'hptraw_response_leadjet' : ['ptraw_response_leadjet','p_{T,raw} - p_{T,gen}(GeV)','events',2], 
                  'hpt_response_leadjet'    : ['pt_response_leadjet','p_{T} - p_{T,gen}(GeV)','events',2],
                  'hptcorr_response_leadjet': ['ptcorr_response_leadjet','p_{T} - p_{T,gen}(GeV)','events',2],
                  'hm_response_leadjet'     : ['m_response_leadjet','m - m_{gen}(GeV)','events',2],
                  'hmconst_response_leadjet': ['mconst_response_leadjet','m - m_{gen}(GeV)','events',2],
                  'hmclean_response_leadjet': ['mclean_response_leadjet','m - m_{gen}(GeV)','events',2],
                  'hmtrim_response_leadjet' : ['mtrim_response_leadjet','m_{trim} - m_{gen}(GeV)','events',2],
                  'hmtrimsafe_response_leadjet': ['mtrimsafe_response_leadjet','m_{trim} - m_{gen}(GeV)','events',2],
                  'hmsoftdrop_response_leadjet': ['msoftdrop_response_leadjet','m - m_{gen}(GeV)','events',2],
                  'hmsoftdropsafe_response_leadjet': ['msoftdropsafe_response_leadjet','m - m_{gen}(GeV)','events',2],

                  'hptraw_leadjet' : ['ptraw_leadjet','p_{T,raw} (GeV)','events',5], 
                  'hpt_leadjet'    : ['pt_leadjet','p_{T} (GeV)','events',5],
                  'hptcorr_leadjet': ['ptcorr_leadjet','p_{T} (GeV)','events',5],
                  'heta_leadjet'   : ['eta_leadjet','#eta','events',2],
                  'hm_leadjet'     : ['m_leadjet','m (GeV)','events',2],
                  'hmconst_leadjet': ['mconst_leadjet','m (GeV)','events',2],
                  'hmclean_leadjet': ['mclean_leadjet','m (GeV)','events',2],
                  'hmtrim_leadjet' : ['mtrim_leadjet','m_{trim} (GeV)','events',2],
                  'hmtrimsafe_leadjet' : ['mtrimsafe_leadjet','m_{trim} (GeV)','events',2],
                  'hmsoftdrop_leadjet': ['msoftdrop_leadjet','m (GeV)','events',2],
                  'hmsoftdropsafe_leadjet': ['msoftdropsafe_leadjet','m (GeV)','events',2],

                  # for pu/good plots
                  'hptraw_pu'      : ['ptraw_pu','p_{T,raw} (GeV)','events',5], 
                  'hpt_pu'         : ['pt_pu','p_{T} (GeV)','events',5],
                  'hptgen_pu'      : ['ptgen_pu','p_{T,gen} (GeV)','events',5],
                  'heta_pu'        : ['eta_pu','#eta','events',2],

                  'hptraw_good'    : ['ptraw_good','p_{T,raw} (GeV)','events',5], 
                  'hpt_good'       : ['pt_good','p_{T} (GeV)','events',5],
                  'hptgen_good'    : ['ptgen_good','p_{T,gen} (GeV)','events',5],
                  'heta_good'      : ['eta_good','#eta','events',2],

                  }


    styles = {} # color, linestyle, line width
    styles['GEN'] = [ROOT.kBlack, 1, 2]
    styles['PUPPI'] = [ROOT.kGreen+1, 1, 2]
    styles['PF'] = [ROOT.kBlue, 1, 2]
    styles['PF+CHS'] = [ROOT.kMagenta, 1, 2]
    styles['PF-CMSSW'] = [ROOT.kOrange, 1, 2]

    
    # -- open file
    f = ROOT.TFile.Open(filename);

    # -- rebin histograms
    for typ, suff in types.iteritems():
        for hname,plotAttributes in histograms.iteritems():
            h = f.Get(suff+'/'+hname+'_'+suff)
            h.Rebin(plotAttributes[3])

    # -- make plots 

    # kin. distributions        
    for histogram, plotAttributes in histograms.iteritems():
        if ('pu' not in histogram and 'good' not in histogram and 'response' not in histogram):
            makeKinComparisonPlots(f, histogram, types, plotAttributes, styles, options.outdir)
    
    # response plots
    for histogram, plotAttributes in histograms.iteritems():
        if ('response' in histogram):
            makeResponseComparisonPlots(f, histogram, types, plotAttributes, styles, options.outdir)

    

    # pu 
    #types.pop('GEN')
    for typ,suff in types.iteritems(): 
        makePileupPlots(f, typ, suff, styles, options.outdir)
        

    makeRealJetFractionPlots(f, types,  styles, options.outdir)    
    makeEfficiencyPlots(f, types, styles, options.outdir)
    
            

    raw_input('ok?')

        
        
