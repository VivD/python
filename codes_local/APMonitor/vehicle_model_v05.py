import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import interpolate

#Drive cycle data
##GEMII with grade
tgem  = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668])
gemII = np.dot (0.44704, np.array([0,0,0,0,0,0,0,0.410031102,1.17998585,2.259980482,3.190100134,3.969897418,4.659993408,5.320114402,5.939970476,6.479967792,6.90990766,7.28012123,7.640044876,8.020100982,8.360115862,8.59991583,8.739948274,8.820030726,8.820030726,8.760080734,8.660089516,8.580007064,8.520057072,8.46010708,8.380024628,8.310008406,8.210017188,8.11002597,7.999968522,7.94001853,7.94001853,7.799986086,7.42999621,6.790007676,5.810004262,4.649927178,3.02993523,1.879924376,1.150010854,1.139944624,1.120035858,1.109969628,1.19005208,1.570108186,2.310087938,3.36995011,4.510118428,5.55991437,6.40995157,7.08998133,7.58993742,7.989902292,8.320074636,8.639957056,8.909955714,9.13007061,9.29001182,9.400069268,9.390003038,9.200086832,8.839939492,8.350049632,7.810052316,7.219947544,6.649975232,6.130110376,5.75005427,5.610021826,5.650063052,5.799938032,5.950036706,6.09006915,6.209969134,6.309960352,6.339935348,6.469901562,6.649975232,6.879932664,7.040097568,7.049940104,7.010122572,6.900065124,6.879932664,6.889998894,6.960015116,7.040097568,7.170063782,7.289963766,7.389954984,7.480103666,7.570028654,7.61006988,7.58993742,7.529987428,7.459971206,7.400021214,7.389954984,7.380112448,7.370046218,7.370046218,7.389954984,7.41992998,7.42999621,7.400021214,7.389954984,7.41992998,7.500012432,7.570028654,7.60000365,7.60000365,7.61006988,7.640044876,7.680086102,7.740036094,7.820118546,7.899977304,7.959927296,7.989902292,8.020100982,8.010034752,7.870002308,7.58993742,7.200038778,6.520009018,5.529939374,4.360019754,3.299933888,2.500004144,1.940098062,1.560041956,0.950028418,0.420097332,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.109969628,2.650102818,4.449944742,5.680038048,6.74996645,7.58993742,7.750102324,7.629978646,7.670019872,8.699907048,10.19999901,11.91998218,12.8400356,13.26997547,13.38003292,13.60999035,14.14998766,14.84008365,16.4900506,18.32993375,20.3599568,21.46992643,22.34993862,22.95995216,23.46013194,23.92004681,24.4200029,24.98997521,25.91002863,26.26010974,26.38000973,26.26010974,26.49006717,26.76006583,27.07010572,26.63994215,25.99011108,24.77008401,24.03994679,23.39011572,22.72999473,22.16002242,21.66006633,21.39006767,21.43010889,20.66999668,17.98007633,13.15007548,7.710061098,3.299933888,0.880012196,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.49995609,1.570108186,3.069976456,4.57006842,5.650063052,6.949948886,8.050075978,9.13007061,10.05012403,11.62000852,12.92011805,13.83994778,14.3799451,15.6400134,17.14010536,18.21003376,18.90012975,19.44012707,20.08995814,21.89002376,24.15000424,26.26010974,26.94998204,27.03006449,27.30006315,28.09999289,29.44014365,30.78007071,32.09002277,33.24003362,34.4600607,35.42015535,35.88007021,36.03016889,35.84002899,35.65011278,35.3100979,35.18997422,35.119958,35.119958,35.04009924,35.08014047,35.04009924,35.3400729,35.50001411,35.77001276,35.81005399,35.92011144,36.23015132,36.42006753,36.65002496,36.26012632,36.06998642,35.84002899,35.96015266,35.9999702,35.57003033,35.00005802,34.08000459,33.3901323,32.20008022,30.32015584,28.480049,26.94998204,26.18002729,25.38009755,24.77008401,23.46013194,22.38997985,20.96997034,20.08995814,18.90012975,18.16999254,16.47998437,15.07004109,12.23002206,10.08009903,7.710061098,7.319938762,8.63011452,10.76997132,12.65011939,13.87998901,15.02999986,15.6400134,16.99000669,17.98007633,19.13008719,18.66994863,18.25007499,18.16999254,18.39994997,19.63004328,20.32013927,21.43010889,21.46992643,21.97010621,22.27007986,22.6899535,23.15009206,23.69008938,23.96008803,24.27012792,24.34014414,24.50008535,24.4200029,24.37996167,24.30994545,24.23008669,24.69000156,25.11009889,25.52997253,25.38009755,24.57994411,23.76994813,23.5399907,23.49994948,24.15000424,24.30010291,24.15000424,23.19013329,22.5000373,21.93006498,21.84998253,21.55000888,21.89002376,21.97010621,21.97010621,22.01014744,21.84998253,21.6200251,21.6200251,22.01014744,22.81007718,23.5399907,24.37996167,24.800059,24.6101428,23.12011706,21.6200251,19.90004193,18.86008853,17.78993643,17.24993912,16.90992424,16.74998303,16.74998303,16.8701067,16.36992692,16.36992692,16.4900506,17.21012158,17.41010402,17.37006279,16.8701067,16.72000803,16.22005194,15.76013708,14.71995998,13.6900728,12.00006463,10.42995644,8.709973278,7.44006244,5.710013044,4.21998731,2.300021708,0.99991218,0,0.610013538,1.19005208,1.609925718,1.53006696,2.340062934,4.290003532,7.24992254,10.19999901,12.45997949,14.53004377,16.22005194,17.87001888,19.74010072,21.01001156,22.23003864,22.61993728,23.61000692,24.88014146,26.15005229,26.99002326,27.55999558,28.18007534,28.93996386,29.83004229,30.78007071,31.82002411,32.78011876,33.24003362,33.46999106,33.31004985,33.08009241,32.78011876,32.38999642,32.130064,31.82002411,31.55002545,31.2500518,30.94001192,30.71005448,30.55995581,30.79013694,31.13015182,31.55002545,31.50998423,31.469943,31.43996801,31.50998423,31.59006668,31.67014913,32.01016401,32.63002009,33.3901323,34.30996203,34.81014181,34.20012827,32.38999642,30.28995715,28.56013145,26.45002595,24.78999277,23.12011706,20.72994667,18.32993375,15.72009585,13.11003426,10.46999767,7.820118546,5.699946814,3.569932546,0.920053422,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.49995609,1.500091964,2.999960234,4.500052198,5.799938032,6.520009018,6.74996645,6.439926566,6.169927908,6.330092812,6.709925224,7.400021214,7.670019872,7.330004992,6.709925224,6.40995157,6.60009147,6.560050244,5.939970476,5.450080616,5.869954254,6.709925224,7.559962424,7.58993742,7.629978646,7.670019872,7.670019872,7.480103666,7.289963766,7.289963766,7.400021214,7.480103666,7.519921198,7.519921198,7.480103666,7.44006244,7.28012123,7.210105008,7.08998133,7.060006334,7.289963766,7.750102324,8.550032068,9.090029384,10.0400578,11.12005243,12.45997949,12.99997681,14.26004511,15.37001474,17.01998168,18.16999254,19.20994594,20.17004059,20.65993045,21.12006901,21.43010889,22.65997851,23.92004681,25.42013877,25.52997253,26.67998338,28.14003412,30.05999972,30.94001192,31.63010791,32.36002143,33.24003362,33.66013096,34.12004582,35.92011144,37.71995336,39.26008655,39.45000276,39.83005886,40.18013997,40.48011363,40.75011229,41.02011094,41.36012582,41.79006569,42.40007923,42.82017656,43.05013399,43.09017522,43.2400502,43.59013131,44.01000495,44.35001983,44.55000226,44.82000092,45.05018205,45.31011448,45.58011313,45.99998677,46.31002666,46.53998409,46.61000031,46.92004019,47.19003885,47.46003751,47.54011996,47.54011996,47.54011996,47.50007874,47.50007874,47.50007874,47.31016253,47.04016387,46.77016521,45.54007191,43.2400502,41.52006703,39.79001764,38.07003447,36.33998508,34.03996337,32.44994642,30.86015316,28.83013011,26.45002595,24.27012792,22.04012243,19.81995948,17.04011414,14.26004511,11.52001731,8.7799895,7.170063782,5.55991437,3.72003122,3.38001634,3.110017682,2.580086596,1.660033174,0.66996353,0,0,0,0,0,0,0,0,0,0,0]))
dis   = np.array([0,402,804,1206,1210,1222,1234,1244,1294,1344,1354,1408,1504,1600,1654,1666,1792,1860,1936,2098,2260,2336,2404,2530,2548,2732,2800,2880,2948,3100,3252,3320,3400,3468,3652,3666,3742,3818,3904,3990,4066,4142,4158,4224,4496,4578,4664,4732,4916,5100,5168,5254,5336,5608,5674,5724,5808,5900,6122,6314,6454,6628,6714,6838,6964,7040,7112,7164,7202,7292,7382,7420,7472,7544,7620,7746,7870,7956,8130,8270,8462,8684,8776,8860,8904,9010,9070,9254,9438,9498,9604,9616,9664,9718,9772,9820,9830,9898,10024,10150,10218,10228,10316,10370,10514,10658,10712,10800,10812,10900,10954,11098,11242,11296,11384,11394,11462,11588,11714,11782,11792,11840,11894,11948,11996,12008,12114,12174,12358,12542,12602,12708,12752,12836,12928,13150,13342,13482,13656,13742,13866,13992,14068,14140,14192,14230,14320,14410,14448,14500,14572,14648,14774,14898,14984,15158,15298,15490,15712,15804,15888,15938,16004,16276,16358,16444,16512,16696,16880,16948,17034,17116,17388,17454,17470,17546,17622,17708,17794,17870,17946,17960,18144,18212,18292,18360,18512,18664,18732,18812,18880,19064,19082,19208,19276,19352,19514,19676,19752,19820,19946,19958,20012,20108,20204,20258,20268,20318,20368,20378,20390,20402,20406,20808,21210,21612])
grade = 0
#grade = np.array([0,0,0.5,0,0,-0.1,0,0,0.36,0,0,-0.28,-1.04,-0.28,0,0,0.39,0.66,1.15,2.44,1.15,0.66,0.39,0,0,-0.46,-0.69,-1.08,-1.53,-2.75,-1.53,-1.08,-0.69,-0.46,0,0,0.35,0.9,1.59,0.9,0.35,0,0,-0.1,-0.69,-0.97,-1.36,-1.78,-3.23,-1.78,-1.36,-0.97,-0.69,-0.1,0,0,0.1,0.17,0.38,0.58,0.77,1.09,1.29,1.66,2.14,2.57,3,3.27,3.69,5.01,3.69,3.27,3,2.57,2.14,1.66,1.29,1.09,0.77,0.58,0.38,0.17,0.1,0,0,-0.38,-0.69,-2.13,-0.69,-0.38,0,0,0.26,0.7,0.26,0,0,-0.34,-1.33,-0.34,0,0,0.37,0.7,1.85,0.7,0.37,0,0,-0.37,-0.7,-1.85,-0.7,-0.37,0,0,0.34,1.33,0.34,0,0,-0.26,-0.7,-0.26,0,0,0.38,0.69,2.13,0.69,0.38,0,0,-0.1,-0.17,-0.38,-0.58,-0.77,-1.09,-1.29,-1.66,-2.14,-2.57,-3,-3.27,-3.69,-5.01,-3.69,-3.27,-3,-2.57,-2.14,-1.66,-1.29,-1.09,-0.77,-0.58,-0.38,-0.17,-0.1,0,0,0.1,0.69,0.97,1.36,1.78,3.23,1.78,1.36,0.97,0.69,0.1,0,0,-0.35,-0.9,-1.59,-0.9,-0.35,0,0,0.46,0.69,1.08,1.53,2.75,1.53,1.08,0.69,0.46,0,0,-0.39,-0.66,-1.15,-2.44,-1.15,-0.66,-0.39,0,0,0.28,1.04,0.28,0,0,-0.36,0,0,0.1,0,0,-0.5,0,0])                  #road grade factor

#Vehicle data
m     = 300                #mass in Kg
load  = 60.0               #total passenger weight in kg
rho   = 1.19               #air density in kg/m^3
A     = 0.7                #area in m^2
Cd    = 0.5                #coefficient of drag dimensionless
Fp    = 30                 #engine power plant force
Fb    = 50                 #brake power plant force
Crr   = 0.005              #rolling resistance factor
wh_rd = 0.265              #dynamic rolling radius in m
Igb_i = 0.02               #gearbox input inertias
Igb_o = 0.02               #gearbox output inertias
Fdr   = 4.71               #final drive ratio
Fef   = 0.9604             #final drive ratio efficiency
wh_inr= 0.4                #wheel inertia rear
wh_inf= 0.35               #wheel inertia front
mdamp = 0.35
vdamp = 0.15
gb    = np.array([1.0,3.65,2.15,1.45,1.0,0.83])
ge    = np.array([0.0,0.95,0.95,0.95,0.95,0.95])
ws    = 0.0
fuel_flow = []

#engine data
eng_i   = 0.1
eng_spd = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000])
eng_trq = np.array([31.93184024, 43.84989124, 52.39157764, 58.77201955, 60.621201, 60.99103728, 59.97387807, 56.73770113, 50.7270955])
eng_brk = np.array([0, -1.619401501, -2.80112692, -3.588943867, -4.245457989, -4.639366462, -5.033274935, -5.252112976, -5.3834158])
ff_spd  = np.array([1000,1000,1000,1000,1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,3000,3000,3000,3000,3000,4000,4000,4000,4000,4000,4000,4000,4000,4000,5000,5000,5000,5000,5000,5000,5000,5000,6000,6000,6000,6000,6000,6000,6000,6000,6000,7000,7000,7000,7000,7000,7000,7000,7000,7000,7000,8000,8000,8000,8000,8000,8000,8000,8000,8000,8000])
ff_trq  = np.array([3.36105906158820,7.96570468008340,14.5308458999320,20.7020786465900,27.0046142176450,33.2196145724360,38.9531712377710,44.6867279031050,47.4979213734450,3.17638601583470,9.01612727525930,15.4937332788440,21.4023603767080,27.7048959477630,34.2700371676120,41.4916925094460,48.0520192924000,53.8341580027620,3.19503539365980,10.0665498704350,16.6316910902840,22.9779942694710,29.3680650567910,35.9332062766400,41.7980657663720,54.2718340840850,62.5439120210950,3.10750017739520,10.5917611680230,17.3757404285340,24.0284168646470,30.5060228682320,36.8085584392870,42.9360235778120,49.4136295813970,64.5572219951820,3.15126778552750,10.5479935598910,17.3757404285340,30.8123961251580,37.5963753856690,45.1244039844290,50.8141930416310,66.1328558879450,3.06373256926290,10.1103174785670,16.7192263065490,23.3719027426620,30.1996496113050,37.3337697368750,43.7238405241940,57.1604962208180,66.1328558879450,2.34535293318290,8.70975401833300,15.8438741439020,22.3214801474870,29.0179241917330,35.5392978034490,42.7609531452830,48.9759535000730,54.8408129898050,63.4630317918740,1.97600684167580,5.29588058401150,12.0798598445220,18.2948601993130,24.2034872971770,30.3747200438350,42.5421151046210,47.6191576479710,52.7399677994540,57.1167286126860])
ff_flow = np.array([0.0118805166666670,0.0137083333333330,0.0162400000000000,0.0205100000000000,0.0247800000000000,0.0289800000000000,0.0342300000000000,0.0385000000000000,0.0409878333333330,0.0130685666666670,0.0166250000000000,0.0217000000000000,0.0268800000000000,0.0322700000000000,0.0380100000000000,0.0449400000000000,0.0534623333333330,0.0619500000000000,0.0173600000000000,0.0245000000000000,0.0331800000000000,0.0408800000000000,0.0484400000000000,0.0573300000000000,0.0641200000000000,0.0880600000000000,0.102620000000000,0.0207200000000000,0.0303800000000000,0.0399700000000000,0.0490700000000000,0.0583800000000000,0.0671300000000000,0.0766500000000000,0.0865900000000000,0.122010000000000,0.0259000000000000,0.0373100000000000,0.0494200000000000,0.0710500000000000,0.0834400000000000,0.0966700000000000,0.108430000000000,0.147910000000000,0.0315700000000000,0.0446600000000000,0.0581000000000000,0.0710500000000000,0.0849100000000000,0.0991900000000000,0.113750000000000,0.156100000000000,0.192640000000000,0.0397996666666670,0.0550200000000000,0.0717500000000000,0.0866600000000000,0.103950000000000,0.120960000000000,0.144060000000000,0.166110000000000,0.195160000000000,0.243740000000000,0.0522743333333330,0.0608300000000000,0.0808500000000000,0.0994700000000000,0.117950000000000,0.139510000000000,0.198240000000000,0.228340000000000,0.260540000000000,0.286020000000000])
ff      = interpolate.interp2d(ff_spd, ff_trq, ff_flow, kind='cubic')

#Simulation time step definition
tf        = tgem[-1]            #final time for simulation
nsteps    = tf*10 + 1           #number of time steps
delta_t   = tf / (nsteps - 1)   #length of each time step
ts        = np.linspace(0,tf,nsteps)

#variables assign
vs        = np.zeros(nsteps)   #variable for actual vehicle speed
acc       = np.zeros(nsteps)
wh_sp     = np.zeros(nsteps)
wh_spt    = np.zeros(nsteps)
gb_op     = np.zeros(nsteps)
gb_opt    = np.zeros(nsteps)
gb_ip     = np.zeros(nsteps)
gb_ipt    = np.zeros(nsteps)
gb_rat    = np.zeros(nsteps)
gb_eff    = np.zeros(nsteps)
eng_sp    = np.zeros(nsteps)
eng_tq    = np.zeros(nsteps)
eng_re    = np.zeros(nsteps)
es        = np.zeros(nsteps)
ies       = np.zeros(nsteps)
sp_store  = np.zeros(nsteps)
act_ped   = np.zeros(nsteps)
test      = np.zeros(nsteps)
f_consp   = np.zeros(nsteps)
v0        = 0.0                #variable for initial velocity
eng_wmin  = 1000
eng_wmax  = 9000
eng_w     = eng_wmin
eng_t     = 0
vgear     = 0.0
t_step    = 0.0
f_var     = 0.0
eng_var   = 0.0

#Desired velocity
def dc(t_step):
    sp = np.interp(t_step,tgem,gemII)
    return sp

#vehicle plant model
def roadload(ws,t,whl_t,u):
    Iw    = ((m + load)*wh_rd**2) + wh_inf + wh_inr
    if u >= 0:
        dw_dt = 1/Iw * (whl_t - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
    else:
        if v0 > 0.1:
            dw_dt = 1/Iw * (Fb*u*wh_rd - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
        else:
            dw_dt = 1/Iw * (Fb*0*wh_rd - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
    return dw_dt

#gear shift plant model & efficiency
def g_box(vgear):
    gvar = 0
    evar = 0
    if u > 0 or u < 0:
        gvar = 1
        evar = ge[gvar]
    else:
        gvar = 0
        evar = ge[gvar]
        
    if vgear > 0.2 and vgear <= 7.15111:
        gvar = 1
        evar = ge[gvar]

    elif vgear > 7.15111 and vgear <= 11.1736:
        gvar = 2
        evar = ge[gvar]

    elif vgear > 11.1736 and vgear <= 17.8778:
        gvar = 3
        evar = ge[gvar]

    elif vgear > 17.8778 and vgear <= 20.5594:
        gvar = 4
        evar = ge[gvar]

    elif vgear > 20.5594:
        gvar = 5
        evar = ge[gvar]

    return gvar, evar  

#engine wide open throttle torque table
def eng_wot(eng_w):
    if u > 0:
        etvar = np.interp(eng_w, eng_spd, eng_trq)
    if u <= 0:
        etvar = np.interp(eng_w, eng_spd, eng_brk)
    return etvar

#def eng_dyn(eng_sp, t):        
    #dw_dt = (vart / eng_i) + (Fc * wh_rd * Fef * Fdr * gear)
    #return dw_dt

#Advanced cyber driver
step      = np.zeros(nsteps)   #assigning array for pedal position
ubias     = 0.0
kc        = 15.0
tauI      = 09.0
sum_int   = 0
sp        = 0
gear      = 1

#Simulation
for i in range(nsteps - 1):
    t_step = ts[i+1]
    sp = dc(t_step)
    error = sp - v0
    es[i+1] = error
    sum_int = sum_int + error * delta_t
    u = ubias + kc*error + tauI * sum_int  #Cyber driver as a PI controller
    ies[i+1] = sum_int
    step[i+1] =100						   #u is accpedal variable and the control param for the engine torque

    if u >= 100.0:
        u = 100.0
        sum_int = sum_int - error * delta_t #anti-windup/clamping
    if u <= -50:
        u = -50
        sum_int = sum_int - error * delta_t #anti-windup/clamping

    if v0 < 0.1 and u < 0:
        act_ped[i+1] = -50
    else:
        act_ped[i+1] = u

    if u > 0:
        eng_tq[i+1]= eng_wot(eng_w) * act_ped[i+1]/100
    if u <= 0:
        eng_tq[i+1]= eng_wot(eng_w)
    eng_var      = eng_tq[i+1]
    gb_rat[i+1], gb_eff[i+1] = g_box(vgear)
    gear         = gb[int(gb_rat[i+1])]
    gb_ipt[i+1]  = eng_tq[i+1] - Igb_i * (gb_ip[i] - gb_ip[i-1])/delta_t #+ vdamp * gb_ip[i] ** 2 + mdamp * gb_ip[i]
    gb_opt[i+1]  = gb_ipt[i+1] * gear * gb_eff[i+1] - Igb_o * (gb_op[i] - gb_op[i-1])/delta_t
    wh_spt[i+1]  = gb_opt[i+1] * Fdr * Fef - (wh_inf + wh_inr) * (wh_sp[i] - wh_sp[i-1])/delta_t
    whl_t        = wh_spt[i+1]
    wh_spd       = odeint(roadload, ws, [0,delta_t], args=(whl_t,u))
    ws           = wh_spd[-1]
    wh_sp[i+1]   = ws
    gb_op[i+1]   = wh_sp[i+1] * Fdr
    gb_ip[i+1]   = gb_op[i+1] * gear
    eng_sp[i+1]  = gb_ip[i+1] * 60 / (2 * np.pi)
    if eng_sp[i+1] < eng_wmin:
        eng_sp[i+1] = eng_wmin
    if eng_sp[i+1] > eng_wmax:
        eng_sp[i+1] = eng_wmax
    eng_w       = eng_sp[i+1]
    vs[i+1]     = wh_sp[i+1] * wh_rd
    v0          = vs[i+1]
    vgear       = vs[i+1]
    acc[i]      = (vs[i+1] - vs[i]) / (delta_t * 9.81)
    f_var       = ff(eng_w,eng_var)
    if f_var < 0: #fuel flow interpolation clipped when below zero
        f_var = 0
    f_consp[i+1]= f_consp[i] + f_var * delta_t / 3600
   
print(f'Top speed in kmph:{max(vs)*3.6: .2f}')

plt.figure()
#plt.clf()
ax=plt.subplot(3,2,1)
ax.grid()
plt.plot(ts,vs,'b-',linewidth=2)
plt.plot(tgem,gemII,'k--',linewidth=2)
plt.ylabel('Velocity [m/s]')
plt.legend(['Velocity [m/s]','Set Point [m/s]'],loc = 'best')

ax=plt.subplot(3,2,2)
ax.grid()
plt.plot(ts,act_ped,'r--',linewidth=2)
plt.ylabel('Gas Pedal')
plt.legend(['Gas Pedal [%]'], loc = 'best')
plt.xlabel('Time (sec)')
    
ax=plt.subplot(3,2,3)
ax.grid()
plt.plot(ts,wh_sp,'b--',linewidth=2)
plt.legend(['Wheel Speed [rpm]'], loc = 'best')
plt.xlabel('Time (sec)')

ax=plt.subplot(3,2,4)
ax.grid()
plt.plot(ts,acc,'k--',linewidth=2)
plt.legend(['Vehicle Acceleration [*g]'], loc = 'best')
plt.xlabel('Time (sec)')

ax=plt.subplot(3,2,5)
ax.grid()
plt.plot(ts,gb_rat,'k-',linewidth=2)
plt.legend(['Current Gear [--]'], loc = 'best')
plt.xlabel('Time (sec)')

ax=plt.subplot(3,2,6)
ax.grid()
plt.plot(ts, eng_sp, 'b-',linewidth=2)
plt.legend(['Engine Speed [rpm]'], loc = 'best')
plt.xlabel('Time (sec)')
plt.draw()
#plt.pause(0.01)
plt.show()
