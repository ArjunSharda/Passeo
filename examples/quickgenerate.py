from passeo import passeo

# Side note: This will create a new .txt file for bulk passwords and quickgenerate passwords by default will also have a new .txt file

print(passeo.quickgenerate(length=10, save=True, bulk=1))
