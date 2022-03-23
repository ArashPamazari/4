adade_aval=int(input('adade aval ra vared konid:  '))
adade_dovom=int(input('adade dovom ra vared konid:  '))

for i in range (1, adade_aval + 1):
	if i <= adade_dovom:
		if adade_aval % i == 0 and adade_dovom % i == 0:
			bmm = i


print ("bozorg tarin mazrab moshtarak : ", bmm)