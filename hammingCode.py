# # Python program to demonstrate
# # hamming code


# def calcRedundantBits(m):

# 	# Use the formula 2 ^ r >= m + r + 1
# 	# to calculate the no of redundant bits.
# 	# Iterate over 0 .. m and return the value
# 	# that satisfies the equation

# 	for i in range(m):
# 		if(2**i >= m + i + 1):
# 			return i


# def posRedundantBits(data, r):

# 	# Redundancy bits are placed at the positions
# 	# which correspond to the power of 2.
# 	j = 0
# 	k = 1
# 	m = len(data)
# 	res = ''

# 	# If position is power of 2 then insert '0'
# 	# Else append the data
# 	for i in range(1, m + r+1):
# 		if(i == 2**j):
# 			res = res + '0'
# 			j += 1
# 		else:
# 			res = res + data[-1 * k]
# 			k += 1

# 	# The result is reversed since positions are
# 	# counted backwards. (m + r+1 ... 1)
# 	return res[::-1]


# def calcParityBits(arr, r):
# 	n = len(arr)

# 	# For finding rth parity bit, iterate over
# 	# 0 to r - 1
# 	for i in range(r):
# 		val = 0
# 		for j in range(1, n + 1):

# 			# If position has 1 in ith significant
# 			# position then Bitwise OR the array value
# 			# to find parity bit value.
# 			if(j & (2**i) == (2**i)):
# 				val = val ^ int(arr[-1 * j])
# 				# -1 * j is given since array is reversed

# 		# String Concatenation
# 		# (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
# 		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
# 	return arr


# def detectError(arr, nr):
# 	n = len(arr)
# 	res = 0

# 	# Calculate parity bits again
# 	for i in range(nr):
# 		val = 0
# 		for j in range(1, n + 1):
# 			if(j & (2**i) == (2**i)):
# 				val = val ^ int(arr[-1 * j])

# 		# Create a binary no by appending
# 		# parity bits together.

# 		res = res + val*(10**i)

# 	# Convert binary to decimal
# 	return int(str(res), 2)


# # Enter the data to be transmitted
# data = '1011'

# # Calculate the no of Redundant Bits Required
# m = len(data)
# r = calcRedundantBits(m)

# # Determine the positions of Redundant Bits
# arr = posRedundantBits(data, r)

# # Determine the parity bits
# arr = calcParityBits(arr, r)

# # Data to be transferred
# print("Data transferred is " + arr)

# # Stimulate error in transmission by changing
# # a bit value.
# # 10101001110 -> 11101001110, error in 10th position.

# arr = '11101001110'
# print("Error Data is " + arr)
# correction = detectError(arr, r)
# print("The position of error is " + str(correction))





# Procedure

# The procedure used by the sender to encode the message encompasses the following steps −

# Step 1 − Calculation of the number of redundant bits.

# Step 2 − Positioning the redundant bits.

# Step 3 − Calculating the values of each redundant bit.


# Decoding a message in Hamming Code

# Once the receiver gets an incoming message, it performs recalculations to detect errors and correct them. The steps for recalculation are −

# Step 1 − Calculation of the number of redundant bits.

# Step 2 − Positioning the redundant bits.

# Step 3 − Parity checking.

# Step 4 − Error detection and correction


option=int(input('Press 1 for generating hamming code  \nPress 2 for finding error in hamming code\n\t Enter your choice:--\n'))

if(option==1):  # GENERATE HAMMING CODE
    print('Enter the data bits')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('Hamming code generated would be:- ', end="")
    print(int(''.join(map(str, h))))


elif(option==2): # DETECT ERROR IN RECEIVED HAMMING CODE
    print('Enter the hamming code received')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        print('There is no error in the hamming code received')

    elif((error)>=len(h_copy)):
        print('Error cannot be detected')

    else:
        print('Error is in',error,'bit')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('After correction hamming code is:- ')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))

else:
    print('Option entered does not exist')

