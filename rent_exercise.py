import statistics
import numpy
from scipy import stats

rent_list = [425,430,430,435,435,435,435,435,440,440,440,440,440,445,445,445,445,445,450,450,450,450,450,450,450,460,460,460,465,465,465,470,470,472,475,475,475,480,480,480,480,485,490,490,490,500,500,500,500,510,510,515,525,525,525,535,549,550,570,570,575,575,580,590,600,600,600,600,615,615]
rent_list_np = numpy.array(rent_list)
median = statistics.median(rent_list)
mean = statistics.mean(rent_list)
mode = statistics.mode(rent_list)
variance = statistics.variance(rent_list)
coefficient_of_variance = (statistics.stdev(rent_list)/mean)*100
twenty_fifth_percentile = numpy.percentile(rent_list_np,25)
fifty_percentile = numpy.percentile(rent_list_np,50)
seventy_fifth_percentile = numpy.percentile(rent_list_np,75)

print("The mean is : ",mean)
print("The median is : ",median)
print("The mode is : ",mode)

res = stats.relfreq(rent_list, numbins=9)
start = res.lowerlimit
gap = res.binsize
cumilative_frequency = res.frequency[0]
print("    Range       Frequency    CF")
for i in range(len(res.frequency)):
    print(str(start)+"-"+str(start+gap)+"    "+str(res.frequency[i]*70)+"    "+str(round(cumilative_frequency*70)))
    if((i+1)<len(res.frequency)):
        cumilative_frequency = cumilative_frequency+res.frequency[i+1]

print("The 25th, 50th and 75th percentile are as follows : ", twenty_fifth_percentile,fifty_percentile,seventy_fifth_percentile)
print("The variance and coefficient of variance are as follows : ",variance,coefficient_of_variance)
