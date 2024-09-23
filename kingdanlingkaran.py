x1,y1 = map(int, input ().split())
xs,ys = map(int, input ().split())
xf,yf = map(int, input ().split())

king = (xs - xf)**2 + (ys - yf)**2
lingkaran = (x1 - xf)**2 + (y1 - yf)**2

if int(lingkaran) > int(king):
    print("Yes")
else:
    print("No")
