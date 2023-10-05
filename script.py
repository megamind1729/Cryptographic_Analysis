freq_english = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]


def ic(s):
    ans = 0
    N = 0
    for i in range(26):
        n_i = s.count(chr(ord('a')+i))
        N += n_i
        ans += n_i * (n_i-1)
    ans = ans/(N*(N-1))
    return ans

def av_ic(s,key_length):
    ans = 0
    l = []
    for i in range(key_length):
        l.append('')
    for i in range(len(s)):
        l[i%key_length] += s[i]
    for i in range(key_length):
        ans += ic(l[i])
    ans = ans/key_length
    return ans 

def find_key_length(s):
    l = []
    max_av_ic = 0
    for i in range(1,13):
        if av_ic(s,i) > max_av_ic:
            ans = i
            max_av_ic = av_ic(s,i) 
    return ans

def freq_list(s):
    freq = []
    for i in range(26):
        freq.append(s.count(chr(ord('a')+i))/len(s))
    return freq
          
def shift(s):
    freq = freq_list(s)
    error_list = []
    for i in range(26):
        error = 0
        for j in range(26):
            error += (freq[(j+i)%26] - freq_english[j]/100)**2
        error_list.append(error)
    
    min_error = min(error_list)
    ans = error_list.index(min_error)
    return ans

def find_key(s):
    key_length = find_key_length(s)
    l = []
    ans = ""
    for i in range(key_length):
        l.append('')
    for i in range(len(s)):
        l[i%key_length] += s[i]
    for i in range(key_length):
        ans += chr(ord('a')+shift(l[i]))
    return ans

def vigenere_decrypt(ciphertext,key):
    j=0
    ans = ""
    for i in ciphertext:
        if i.isalpha():
            if(i>='A' and i <= 'Z'):
                if(ord(i)-ord(key[j])+ord('a')<ord('A')):
                    ans += chr(ord(i)-ord(key[j])+ord('a')+26)
                else:
                    ans += chr(ord(i)-ord(key[j])+ord('a'))
            else:
                if(ord(i)-ord(key[j])<0):
                    ans += chr(ord(i)-ord(key[j])+ord('a')+26)
                else:
                    ans += chr(ord(i)-ord(key[j])+ord('a'))
    
            j = (j+1)%len(key)
        else:
            ans = ans + i

    return ans

def main():
    file_path = input("Enter file path: ")
    with open(file_path, 'r') as f:
        ciphertext = f.read()

    s = ""
    for i in ciphertext.lower():
        if i.isalpha():
            s = s+i

    key = find_key(s)
    decrypted_text = vigenere_decrypt(ciphertext,key)
    print("Plaintext:")
    print(decrypted_text)
    print("\nKey:", key)

main()
