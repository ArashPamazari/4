adade_aval=int(input('adade aval ra vared konid:  '))
adade_dovom=int(input('adade dovom ra vared konid:  '))

for i in range (1, adade_aval + 1):
	if i <= adade_dovom:
		if adade_aval % i == 0 and adade_dovom % i == 0:
			bmm = i

kmm = (adade_aval * adade_dovom) / bmm
print ("kochek tarin mazrab moshtarak : ", kmm)