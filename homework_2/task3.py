error = "invalide input"
def posscomb(code):
    letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':'_'}

    def backtrack(code, path, res):
        if (code == ''):
            res.append(path)
            return
        for letter in letters[code[0]]:
            path += letter
            backtrack(code[1:], path, res)
            path = path[:-1]

    res = []
    backtrack(code, '', res)
    return res

def checkcorr(code):
	if(code.isdigit() == False):
		return error
    
print ("enter code:")
inputcode = str(raw_input())
checkcorr(inputcode)
print(posscomb(inputcode))