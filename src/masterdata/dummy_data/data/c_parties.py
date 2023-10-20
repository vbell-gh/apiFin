from datetime import datetime
from src.masterdata.models.c_parties import CounterPartiesMain, CounterpartiesAttribs  


dummy_cparty_main_1 = CounterPartiesMain(
    vatid="123456789",
    country="US",
    company_id=1,
    bank_account="1234567890",
    company_name_cyrilic="Company A",
    company_name_latin="CompanyA",
    address="123 Main St"
)

dummy_cparty_attribs_1 = CounterpartiesAttribs(
    c_id=1,
    is_client=True,
    client_is_due=True,
    client_due_days=30,
    is_vendor=False,
    vendor_is_due=False,
    vendor_due_days=None,
    is_active=True,
    date_deactivation=None,
    date_created=datetime.now(),
    main_contact_name="John Doe",
    main_contact_email="john.doe@example.com",
    main_contact_phone="123-456-7890",
    fin_contact_name="Jane Smith",
    fin_contact_email="jane.smith@example.com",
    fin_contact_phone="987-654-3210",
    upload_one_name="Document 1",
    upload_one_file="path/to/document1.pdf",
    upload_two_name="Document 2",
    upload_two_file="path/to/document2.pdf",
    upload_three_name="Document 3",
    upload_three_file="path/to/document3.pdf",
    creator_id=1
)

dummy_cparty_main_2 = CounterPartiesMain(
    vatid="987654321",
    country="UK",
    company_id=2,
    bank_account="9876543210",
    company_name_cyrilic="Company B",
    company_name_latin="CompanyB",
    address="456 Elm St"
)

dummy_cparty_attribs_2 = CounterpartiesAttribs(
    c_id=2,
    is_client=False,
    client_is_due=False,
    client_due_days=None,
    is_vendor=True,
    vendor_is_due=True,
    vendor_due_days=45,
    is_active=True,
    date_deactivation=None,
    date_created=datetime.now(),
    main_contact_name="Alice Johnson",
    main_contact_email="alice.johnson@example.com",
    main_contact_phone="555-555-5555",
    fin_contact_name="Bob Wilson",
    fin_contact_email="bob.wilson@example.com",
    fin_contact_phone="111-111-1111",
    upload_one_name="Document 4",
    upload_one_file="path/to/document4.pdf",
    upload_two_name="Document 5",
    upload_two_file="path/to/document5.pdf",
    upload_three_name="Document 6",
    upload_three_file="path/to/document6.pdf",
    creator_id=2
)

dummy_cparty_main_3 = CounterPartiesMain(
    vatid="987123456",
    country="CA",
    company_id=3,
    bank_account="9871234560",
    company_name_cyrilic="Company C",
    company_name_latin="CompanyC",
    address="789 Oak St"
)

dummy_cparty_attribs_3 = CounterpartiesAttribs(
    c_id=3,
    is_client=True,
    client_is_due=True,
    client_due_days=60,
    is_vendor=True,
    vendor_is_due=True,
    vendor_due_days=60,
    is_active=True,
    date_deactivation=None,
    date_created=datetime.now(),
    main_contact_name="Mary Johnson",
    main_contact_email="mary.johnson@example.com",
    main_contact_phone="888-888-8888",
    fin_contact_name="Tom Wilson",
    fin_contact_email="tom.wilson@example.com",
    fin_contact_phone="222-222-2222",
    upload_one_name="Document 7",
    upload_one_file="path/to/document7.pdf",
    upload_two_name="Document 8",
    upload_two_file="path/to/document8.pdf",
    upload_three_name="Document 9",
    upload_three_file="path/to/document9.pdf",
    creator_id=2
)

dummy_cparty_main_4 = CounterPartiesMain(
    vatid="654321987",
    country="FR",
    company_id=4,
    bank_account="6543219870",
    company_name_cyrilic="Company D",
    company_name_latin="CompanyD",
    address="987 Pine St"
)

dummy_cparty_attribs_4 = CounterpartiesAttribs(
    c_id=4,
    is_client=False,
    client_is_due=False,
    client_due_days=None,
    is_vendor=False,
    vendor_is_due=False,
    vendor_due_days=None,
    is_active=False,
    date_deactivation=datetime(2023, 3, 1),
    date_created=datetime.now(),
    main_contact_name="Eva Martinez",
    main_contact_email="eva.martinez@example.com",
    main_contact_phone="777-777-7777",
    fin_contact_name="Chris Taylor",
    fin_contact_email="chris.taylor@example.com",
    fin_contact_phone="333-333-3333",
    upload_one_name="Document 10",
    upload_one_file="path/to/document10.pdf",
    upload_two_name="Document 11",
    upload_two_file="path/to/document11.pdf",
    upload_three_name="Document 12",
    upload_three_file="path/to/document12.pdf",
    creator_id=2
)

dummy_cparty_main_5 = CounterPartiesMain(
    vatid="456789123",
    country="DE",
    company_id=5,
    bank_account="4567891230",
    company_name_cyrilic="Company E",
    company_name_latin="CompanyE",
    address="456 Birch St"
)

dummy_cparty_attribs_5 = CounterpartiesAttribs(
    c_id=5,
    is_client=True,
    client_is_due=True,
    client_due_days=45,
    is_vendor=True,
    vendor_is_due=True,
    vendor_due_days=45,
    is_active=True,
    date_deactivation=None,
    date_created=datetime.now(),
    main_contact_name="Paula Davis",
    main_contact_email="paula.davis@example.com",
    main_contact_phone="666-666-6666",
    fin_contact_name="Mark Turner",
    fin_contact_email="mark.turner@example.com",
    fin_contact_phone="444-444-4444",
    upload_one_name="Document 13",
    upload_one_file="path/to/document13.pdf",
    upload_two_name="Document 14",
    upload_two_file="path/to/document14.pdf",
    upload_three_name="Document 15",
    upload_three_file="path/to/document15.pdf",
    creator_id=1
)
c_parties_main_dummies = [v for k, v in vars().items() if k.startswith("dummy_cparty_main")]
c_parties_attribs_dummies = [v for k, v in vars().items() if k.startswith("dummy_cparty_attribs")]