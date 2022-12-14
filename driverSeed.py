
d1 = Driver(
    driverCliNumber=100,
    driverType='OwnerOperator',
    firstName='Bob',
    LastName='Builder',
    homePhone='(310)-987-1327',
    cellPhone='(310)-987-1327',
    startDate='2022-01-01',
    RegistrationExpires='2022-01-01',
    terminated=False,
    terminatedDate='2023-04-01',
    licenseNumber='abc123',
    image='img/project1.png')

d2 = Driver(
    driverCliNumber=101,
    driverType='Driver',
    firstName='driver1',
    LastName='lastName1',
    homePhone='(310)-987-1327',
    cellPhone='(310)-987-1327',
    startDate='2022-01-01',
    RegistrationExpires='2022-01-01',
    terminated=False,
    terminatedDate='2023-04-01',
    licenseNumber='abc1234',
    image='img/project1.png')

d3 = Driver(
    driverCliNumber=102,
    driverType='Driver',
    firstName='driver2',
    LastName='lastName2',
    homePhone='(310)-987-1327',
    cellPhone='(310)-987-1327',
    startDate='2022-01-01',
    RegistrationExpires='2022-01-01',
    terminated=False,
    terminatedDate='2023-04-01',
    licenseNumber='abc1235',
    image='img/project1.png')

c3 = Contractor(
    startDate='2022-01-01',
    contractorBusinessName='2022-01-01',
    firstName=False,
    lastName='2023-04-01',
    city='abc1235',
    addressNumber=123,
    addressLocation='abc1235',
    state='CA',
    zip='abc1235')

<a href = "{% url 'contractors:contractor_detail' contractor.pk %}" class = "btn btn-primary" >
{% url 'contractors:contractor_detail' contractor.pk % }
