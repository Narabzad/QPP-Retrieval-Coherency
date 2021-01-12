import  scipy, numpy, sys

from  scipy import  stats


import getopt, sys
def corr(Actual_file,Predicted_file,corr_type):
    Actual = {}
    Predicted = {}
    with open(Actual_file) as f:
        for line in f:
           (key, val) = line.split()
           Actual[int(key)] = val
    with open(Predicted_file) as f:
        for line in f:
            (key, val) = line.rstrip().strip().split(' ')
            Predicted[int(key)] = val

    actual_ar=[]
    predicted_ar=[]
    for key in Predicted.keys() :
        try:
            actual_ar.append(float(Actual[key]))
            predicted_ar.append(float(Predicted[key]))
        except:
            pass
    pearson=scipy.stats.pearsonr(predicted_ar,actual_ar)
    kendall=scipy.stats.kendalltau(predicted_ar,actual_ar)

    if corr_type=='p':
        return (pearson[0])
    elif corr_type == 'k':
        return (kendall[0])




def fold_cor_eval (corpus,density_measure,classic_method):
    '''if density_metric =='D':
        density_metric='density'
    elif density_metric ='WD':
        density_metric=
    elif density_metric ='ACC':
        density_metric='clustering'
    elif density_metric ='WACC':
        density_metric=
    elif density_metric ='ADC':
        density_metric='degree_connectivity'
    elif density_metric ='WADC':
        density_metric=
    elif density_metric ='AND':
        density_metric=
    elif density_metric ='WAND':
        density_metric=
    elif density_metric='none'
        density_metric='none'''''

    res_p = []
    res_k=[]
    for i in range(10):
        if density_measure !='':
            file='results/'+corpus+'/fold_'+str(i)+'/'+classic_method+'_'+density_measure+'_'+str(i)
        else:
            file = 'results/' + corpus + '/fold_' + str(i) + '/' + density_measure +  '_' + str(i)

        res_p.append(corr('QL run MAP/'+corpus+'_QL.txt',file,'p'))
        res_k.append(corr('QL run MAP/'+corpus+'_QL.txt',file,'k'))

    print('Pearson rho=',numpy.mean(res_p),'\t Kendall tau',numpy.mean(res_k))




full_cmd_arguments = sys.argv

argument_list = full_cmd_arguments[1:]

short_options = "hb:d:c:"
long_options = ["help", "density", "baseline","corpus"]
help=0

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-b", "--baseline"):
        if current_value not in ['WIG', 'Clarity', 'NQC', 'QF', 'ISD', 'SD', 'SMV']:
            print('Baseline value not recognized ')
        else:
            print (("Baseline= %s") % (current_value))
            baselineQPP=current_value
    elif current_argument in ("-d", "--density"):
        if current_value not in ['ACC','ADC','D','AND','WD','WAND','WACC','WADC','none']:
            print('Density value not recognized ')
        else:
            print (("Density=%s") % (current_value))
            density_metric=current_value
    elif current_argument in ("-c", "--corpus"):

        if current_value not in ['rb04','gov2','cw09']:
            print('Corpus value not recognized ')
        else:
            print (("Corpus=%s") % (current_value))
            Corpus=current_value
    elif current_argument in ("-h", "--help"):
        help=1
        print("evaluate.py -c  corpus -b baseline -d density_metric")
        print("choose corpus from ['rb04','gov2','cw09']")
        print("choose density_metric from ['ACC','ADC','AND','D','WACC','WAND',,'WADC','none']:")
        print("choose QPP baseline from ['WIG', 'Clarity', 'NQC', 'QF', 'ISD', 'SD', 'SMV']")

if help==0:
    try:
        fold_cor_eval(Corpus,density_metric,baselineQPP)
    except:
        print("ERROR! please check you inputs... ")