data = hex(int(input(),16))


for index in range(1,16):
    print(
         '%X' % int(data,16)+
         '*'+
         '%X' % int(hex(index),16)+
         '='+
         '%X' % int(hex(int(data,16)*index),16)
    )



#print( f'{255:#x}', f'{255:x}', f'{255:X}' )
#print( '%#x' % 255, '%x' % 255, '%X' % 255 )
#print( format(255, '#x'), format(255, 'x'), format(255, 'X') )