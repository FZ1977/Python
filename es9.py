#Uso della ricerca per bisezione per approssimare la radice quadrata

x=-25
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print("basso=", low, "alto =", high, "ans =", ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print("numero di congetture = ", num_guesses)
print(ans, "e' vicino alla radice quadrata di ", x)
