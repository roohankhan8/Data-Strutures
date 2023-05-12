import numpy_financial as npf 

'''
fv future value
rate of intrest
nper = number of periods
pmt = periodic payments
npf.pv = present value
'''
res=npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
print(res)