from faker import Faker

fake_date =  Faker()

name = fake_date.name();
address = fake_date.address();
email = fake_date.email();

print('\n')

profile = fake_date.simple_profile()
for k,v in profile.items():
    print('[{}, {}'.format(k,v))

print('\n')

print ('Name: {} \nAddress:{} \nEmail: {}'.format(name,address,email))

for _ in range (200):
    print(fake_date.name())

print('\n')