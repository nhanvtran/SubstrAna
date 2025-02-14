#include <iostream>
#include <vector>
#include <assert.h>  
#include "fastjet/PseudoJet.hh"
#include "../include/GenLoader.hh"

using namespace baconhep;

GenLoader::GenLoader(TTree *iTree) { 
  fGenInfo  = new TGenEventInfo();
  fGenInfoBr = 0;
  iTree->SetBranchAddress("GenEvtInfo",       &fGenInfo, &fGenInfoBr);
  //fGenInfoBr  = iTree->GetBranch("GenEvtInfo");

  fGens  = new TClonesArray("baconhep::TGenParticle");
  fGenBr = 0;
  iTree->SetBranchAddress("GenParticle",       &fGens, &fGenBr);
  //fGenBr  = iTree->GetBranch("GenParticle");

  // define charges of pdgIds                                                                                                                                                         
  neutralsPdgId_.push_back( 22 ) ; // photon                                                                                                                              
  neutralsPdgId_.push_back( 130 ); // KLong                                                                                                                                            
  neutralsPdgId_.push_back( 310 ); // KShort                                                                                                                                              
  neutralsPdgId_.push_back( 311 ); // anti-KLong                                                                                                                                          
  neutralsPdgId_.push_back( 111 ); // pi0                                                                                                                                                 
  neutralsPdgId_.push_back( 1 );   // quarks                                                                                                                                              
  neutralsPdgId_.push_back( 2 );
  neutralsPdgId_.push_back( 3 );
  neutralsPdgId_.push_back( 4 );
  neutralsPdgId_.push_back( 5 );
  neutralsPdgId_.push_back( 16 );
  neutralsPdgId_.push_back( -1 );
  neutralsPdgId_.push_back( -2 );
  neutralsPdgId_.push_back( -3 );
  neutralsPdgId_.push_back( -4 );
  neutralsPdgId_.push_back( -5 );
  neutralsPdgId_.push_back( -16 );
  neutralsPdgId_.push_back( 2112 ); // neutron                                                                                                                                          
  
  positivePdgId_.push_back( 321 ); // K+                                                                                                                                                  
  positivePdgId_.push_back( 211 ); // Pi +                                                                                                                                                
  positivePdgId_.push_back( -11 ); // e+                                                                                                                                                  
  positivePdgId_.push_back( -13);  // mu+                                                                                                                                                 
  positivePdgId_.push_back( -15);  // tau+                                                                                                                                                
  positivePdgId_.push_back( 2212);  // proton                                                                                                                                        

  negativePdgId_.push_back( -321 ); // K-                                                                                                                                                 
  negativePdgId_.push_back( -211 ); // Pi -                                                                                                                                               
  negativePdgId_.push_back( 11 );   // e-                                                                                                                                                 
  negativePdgId_.push_back( 13 );   // mu-                                                                                                                                                
  negativePdgId_.push_back( 15 );   // tau-                                                                                                                                              
  negativePdgId_.push_back( -2212);  // anti-proton                                                                                                       

}
GenLoader::~GenLoader() { 
  delete fGenInfo;
  delete fGenInfoBr;

  delete fGens;
  delete fGenBr;
}
void GenLoader::reset() { 
  fQ     = 0;
  fPId1  = 0;
  fX1    = 0;
  fPdf1  = 0;
  fPId2  = 0;
  fX2    = 0;
  fPdf2  = 0;

  fVPt   = 0; 
  fVEta  = 0; 
  fVPhi  = 0; 
  fVM    = 0; 
  fVId   = 0; 
  
  fPt1   = 0; 
  fEta1  = 0; 
  fPhi1  = 0; 
  fM1    = 0; 
  fId1   = 0; 

  fPt2   = 0; 
  fEta2  = 0; 
  fPhi2  = 0; 
  fM2    = 0; 
  fId2   = 0; 
  
  eta_Boson.clear();
  phi_Boson.clear();
  pt_Boson.clear();
}
void GenLoader::setupTree(TTree *iTree) { 
  reset();
  fTree = iTree;
  //fTree->Branch("processId", &processId_ , "processId/I");
  fTree->Branch("Q"          ,&fQ   , "fQ/F");
  fTree->Branch("id1"        ,&fPId1, "fPId1/F");
  fTree->Branch("x1"         ,&fX1  , "fX1/F");
  fTree->Branch("pdf1"       ,&fPdf1, "fPdf1/F");
  fTree->Branch("id2"        ,&fPId2, "fPId2/F");
  fTree->Branch("x2"         ,&fX2  , "fX2/F");
  fTree->Branch("pdf2"       ,&fPdf2, "fPdf2/F");
 
  fTree->Branch("genvpt"   ,&fVPt  ,"fVPt/F");
  fTree->Branch("genveta"  ,&fVEta ,"fVEta/F");
  fTree->Branch("genvphi"  ,&fVPhi ,"fVPhi/F");
  fTree->Branch("genvm"    ,&fVM   ,"fVM/F");
  fTree->Branch("genvid"   ,&fVId  ,"fVId/I");

  fTree->Branch("genpt_1"  ,&fPt1 ,"fPt1/F");
  fTree->Branch("geneta_1" ,&fEta1,"fEta1/F");
  fTree->Branch("genphi_1" ,&fPhi1,"fPhi1/F");
  fTree->Branch("genm_1"   ,&fM1  ,"fM1/F");
  fTree->Branch("genid_1"  ,&fId1 ,"fId1/I");

  fTree->Branch("genpt_2"  ,&fPt2 ,"fPt2/F");
  fTree->Branch("geneta_2" ,&fEta2,"fEta2/F");
  fTree->Branch("genphi_2" ,&fPhi2,"fPhi2/F");
  fTree->Branch("genm_2"   ,&fM2  ,"fM2/F");
  fTree->Branch("genid_2"  ,&fId2 ,"fId2/I");
}
void GenLoader::load(int iEvent) { 
  fGens     ->Clear();
  fGenBr    ->GetEntry(iEvent);
  fGenInfoBr->GetEntry(iEvent);
}
fastjet::PseudoJet GenLoader::convert(TGenParticle *iPart) { 
  double Px    = iPart->pt*cos(iPart->phi);
  double Py    = iPart->pt*sin(iPart->phi);
  double theta = 2*atan(exp(-iPart->eta)); //eta = -ln(tan(theta/2))
  double Pz    = iPart->pt/tan(theta);
  double E     = sqrt(Px*Px+Py*Py+Pz*Pz+iPart->mass*iPart->mass);
  fastjet::PseudoJet tmp_psjet(Px, Py, Pz, E);
  return tmp_psjet;
}

std::vector<fastjet::PseudoJet>  GenLoader::genFetch() { 
  std::vector<fastjet::PseudoJet> genparticles;
  //Second Lets get the Gen Particles
  for( int i1 = 0; i1 < fGens->GetEntriesFast(); i1++){//9,entries loop,fill the vector particles with PF particles
    baconhep::TGenParticle *pPartTmp = (baconhep::TGenParticle*)((*fGens)[i1]);
    if(pPartTmp->status != 1) continue;
    //Convert gen particle to PseudoJet
    fastjet::PseudoJet pFastJet = convert(pPartTmp);
    //Build the collection 
    int charge = getPdgIdCharge( pPartTmp->pdgId ); 
    pFastJet.set_user_index(charge);
    genparticles.push_back(pFastJet);
  }
  return genparticles;
}

int GenLoader::leptonicBosonFilter(fastjet::PseudoJet& leptonVector) { 
  int found = 0;
  int leptonPosition = -1 ;
  std::vector<int> Windices;
  //Second Lets get the Gen Particles
  for( int i1 = 0; i1 < fGens->GetEntriesFast(); i1++){//9,entries loop,fill the vector particles with PF particles
    baconhep::TGenParticle *pPartTmp = (baconhep::TGenParticle*)((*fGens)[i1]);
    if (fabs(pPartTmp->pdgId) == 24 ){
      Windices.push_back(i1);
      //std::cout << "particle " << i1 << ": " << pPartTmp->pdgId << " " << pPartTmp->status << " " << pPartTmp->parent << std::endl;
    }
    if (fabs(pPartTmp->pdgId) == 13 || fabs(pPartTmp->pdgId) == 11 || fabs(pPartTmp->pdgId) == 15){
      for (unsigned int j = 0; j < Windices.size(); j++){
        if (pPartTmp->parent == Windices[j]){ found ++; leptonPosition = i1; }
      }
      if(found > 1) return -1 ;
      //std::cout << "particle " << i1 << ": " << pPartTmp->pdgId << " " << pPartTmp->status << " " << pPartTmp->parent << std::endl;
    }    
  }

  if(leptonPosition != -1) leptonVector  = convert((baconhep::TGenParticle*)((*fGens)[leptonPosition]));
  //std::cout << "fond = " << found << std::endl;
  return found;
}

void GenLoader::fillGenEvent() { 
  fQ    = fGenInfo->scalePDF; 
  fX1   = fGenInfo->x_1; 
  fX2   = fGenInfo->x_2; 
  fPId1 = fGenInfo->id_1; 
  fPId2 = fGenInfo->id_2; 
}
void GenLoader::selectBoson(int PdgIdBoson) {
  reset(); 
  TGenParticle *lBoson   = 0; 
  TGenParticle *lLep1    = 0; 
  TGenParticle *lLep2    = 0; 
  int   lBosonId = -10; 
  bool found = false; 
  for  (int i0 = 0; i0 < fGens->GetEntriesFast(); i0++) { 
    TGenParticle *pGen = (TGenParticle*)((*fGens)[i0]);
	if(  fabs(pGen->pdgId) == PdgIdBoson ) { 
      found = true;
      lBoson   = pGen;
      eta_Boson.push_back(lBoson -> eta);
      phi_Boson.push_back(lBoson -> phi);
      pt_Boson.push_back(lBoson -> pt);
      lBosonId = i0;
    }
    if(pGen->parent == lBosonId) { //All of these guys have two daughters
      //!!!Note this will not work for taus
      if(pGen->status == 1 && lLep1 != 0) lLep2 = pGen;
      if(pGen->status == 1 && lLep1 == 0) lLep1 = pGen;
      if(pGen->status != 1 && lLep1 != 0) lLep2 = getStatus1(i0);  //Obtain the simulation level if not already
      if(pGen->status != 1 && lLep1 == 0) lLep1 = getStatus1(i0); 
      
    }
    
 
  }
  if (found)
  {
    fVPt  = lBoson->pt;  
    fVEta = lBoson->eta; 
    fVPhi = lBoson->phi;
    fVM   = lBoson->mass;
    fVId  = lBoson->pdgId;

    if(lLep1 == 0 || lLep2 == 0) return;
    assert(lLep1);
    assert(lLep2);
    if(lLep2->pt > lLep1->pt || isNeutrino(lLep1)) {  
      TGenParticle *lLep = 0; 
      lLep = lLep1; 
      //Swaps
      lLep1 = lLep2;
      lLep2 = lLep;
    }

    fPt1  = lLep1->pt;
    fEta1 = lLep1->eta;
    fPhi1 = lLep1->phi;
    fM1   = lLep1->mass;
    fId1  = lLep1->pdgId;

    fPt2  = lLep2->pt;
    fEta2 = lLep2->eta;
    fPhi2 = lLep2->phi;
    fM2   = lLep2->mass;
    fId2  = lLep2->pdgId;
  }
}

//H=>ZZ Mu Id
TGenParticle* GenLoader::getStatus1(int iId) { 
  int lId = iId;
  TGenParticle *lGen = 0; 
  for  (int i0 = 0; i0 < fGens->GetEntriesFast(); i0++) { 
    TGenParticle *pGen = (TGenParticle*)((*fGens)[i0]);
    if(pGen->parent == lId) { 
      lGen = pGen;
      if(pGen->status == 1) break; 
      lId = i0;  //Keep searching down the chain for status 1 !!! Assumes gen particle list is ordered
    }
  }    
  //assert(lGen); 
  //assert(lGen->status == 1); ===> commented out to fix issues with taus 
  return lGen;
}
bool GenLoader::isNeutrino(TGenParticle *iPart) { 
  if(fabs(iPart->pdgId) == 12) return true; 
  if(fabs(iPart->pdgId) == 14) return true; 
  if(fabs(iPart->pdgId) == 16) return true; 
  return false;
}


///////////////////////                                                                                                                                                                    
double GenLoader::getPdgIdCharge( const double & fid ){

  double qq = -99.;
  int id = (int) fid;
  if (std::find(neutralsPdgId_.begin(), neutralsPdgId_.end(), id) != neutralsPdgId_.end()) qq = 0.;
  else if (std::find(positivePdgId_.begin(), positivePdgId_.end(), id) != positivePdgId_.end()) qq = 1.;
  else if (std::find(negativePdgId_.begin(), negativePdgId_.end(), id) != negativePdgId_.end()) qq = -1.;
  else return 0;
  return qq;
}

