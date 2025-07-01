import pandas as pd
import numpy as np
import random
from faker import Faker
from faker.providers import date_time, internet
from datetime import datetime, timedelta
import uuid

# ===== SEEDING =====
np.random.seed(42)
random.seed(42)
fake = Faker()
fake_fr = Faker('fr_FR')
fake_uk = Faker('en_GB')
fake_us = Faker('en_US')
fake_cn = Faker('zh_CN')

# ==== HELPER DATA & FUNCTIONS =====
country_list = [
    {'id': 1, 'code': 'NG',   'name': 'Nigeria'},
    {'id': 2, 'code': 'UK',   'name': 'United Kingdom'},
    {'id': 3, 'code': 'US',   'name': 'United States'},
    {'id': 4, 'code': 'FR',   'name': 'France'},
    {'id': 5, 'code': 'CN',   'name': 'China'}
]
currency_list = [
    {'id': 1, 'code': 'NGN',  'name': 'Nigerian Naira'},
    {'id': 2, 'code': 'GBP',  'name': 'Pound Sterling'},
    {'id': 3, 'code': 'USD',  'name': 'US Dollar'},
    {'id': 4, 'code': 'EUR',  'name': 'Euro'},
    {'id': 5, 'code': 'CNY',  'name': 'Chinese Yuan'},
    # dirty/legacy codes
    {'id': 6, 'code': 'EURO', 'name': 'Euro (legacy)'},
    {'id': 7, 'code': 'YUAN', 'name': 'Yuan (nonstandard)'},
    {'id': 8, 'code': 'UKP',  'name': 'Pound (legacy)'},
    {'id': 9, 'code': 'USDOLL', 'name': 'US Dollar (dirty)'}
]
kyc_status_choices = ['PASSED', 'FAILED', 'PENDING', 'FLAGGED', '', None]
remittance_status_choices = ['PENDING', 'COMPLETED', 'FAILED', 'CANCELLED']
transaction_status_choices = ['SUCCESS', 'FAILED', 'REVERSED', 'PENDING']
remittance_methods = ['BANK_TRANSFER', 'MOBILE_MONEY', 'CASH_PICKUP', 'CARD', 'CRYPTO', 'AGENT', '', None]

compliance_types = [
    'AML Threshold', 'PEP Screening', 'Sanctions List', 'KYC Check', 'Geo IP Mismatch', 'Manual Review'
]
compliance_notes = [
    "BVN mismatch", "KYC doc expired", "Transaction flagged", "SAR filed", "Name mismatch",
    "OFAC checked", "Passport expired", "NIN not found", "", "—", "😀", "ID exp", "review…", None
]

officer_names = [
    # regionally appropriate officer/system names
    "Adeolu Oladele", "Sade Bello", "Sarah Thomas", "Mei Zhang", "Jean Dupont", "Tom Smith",
    "Amira Al-Fayed", "Anna Kowalska", "system", "bot", "", "aml_checker@fintech.com", None
]

nigerian_first = [
    # Yoruba, Igbo, Hausa + common
    'Chinedu', 'Ngozi', 'Temitope', 'Adebayo', 'Uche', 'Oluwatoyin', 'Ifeanyi', 'Chidera', 'Nneka', 'Yakubu', 'Zainab'
]
nigerian_last = [
    'Okafor', 'Balogun', 'Adetokunbo', 'Obi', 'Babatunde', 'Abubakar', 'Nwachukwu', 'Eze', 'Akinwale', 'Olawale', 'Abiola'
]

diaspora_name_sets = {
    'NG': (nigerian_first, nigerian_last),
    'IN': (['Priya', 'Amit', 'Neha', 'Rahul', 'Aisha'], ['Patel', 'Kumar', 'Singh', 'Khan', 'Sharma']),
    'PK': (['Fatima', 'Omar', 'Zara', 'Bilal', 'Hassan'], ['Ali', 'Hussain', 'Iqbal', 'Ahmed', 'Malik']),
    'PL': (['Anna', 'Jan', 'Piotr', 'Katarzyna'], ['Nowak', 'Kowalski', 'Lewandowski']),
    'GH': (['Kwame', 'Afia', 'Yaw', 'Akua'], ['Mensah', 'Boateng', 'Owusu']),
    'AR': (['Layla', 'Mohammed', 'Samira', 'Omar'], ['Al-Farsi', 'Rahman', 'Hassan']),
    'CN': (['Mei', 'Wei', 'Li', 'Ying'], ['Wang', 'Li', 'Zhang', 'Liu'])
}
diaspora_prob = 0.15

# Dates
start_date = datetime.now() - timedelta(days=2*365)
end_date = datetime.now() + timedelta(days=30)

def random_date(start, end):
    """Random date, out-of-order, past/future."""
    delta = end - start
    int_delta = delta.days * 24 * 60 * 60
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def make_nigerian_address():
    street = random.choice(['Ikeja', 'Lekki', 'Victoria Island', 'Maitama', 'Wuse', 'Yaba', 'Ikoyi', 'Surulere', 'Asokoro'])
    city = random.choice(['Lagos', 'Abuja', 'Port Harcourt', 'Enugu', 'Ibadan'])
    house = f"{random.randint(1,299)} {random.choice(['Road', 'Ave', 'Street', 'Close'])}"
    return f"{house}, {street}, {city}, Nigeria"

def make_corrupted(val):
    """Randomly corrupt or dirty a value."""
    if val is None or random.random() > 0.08:
        return val
    corruptions = [
        lambda s: s[:random.randint(2,5)],  # Truncate
        lambda s: s + random.choice(['#', '...', ' 😀', '??']),  # Add emoji/symbol
        lambda s: ''.join([c if random.random() > 0.1 else random.choice(['*', '?', '']) for c in s]), # Garble
        lambda s: None,
        lambda s: ''  # Empty
    ]
    return random.choice(corruptions)(str(val))

def maybe_dirty(val, prob=0.07):
    """Dirty a value with given probability."""
    if random.random() < prob:
        return make_corrupted(val)
    return val

def random_phone(country_code):
    if country_code == 'NG':
        return '+234' + ''.join(random.choices('0123456789', k=10))
    if country_code == 'UK':
        return '+44' + ''.join(random.choices('0123456789', k=10))
    if country_code == 'US':
        return '+1' + ''.join(random.choices('0123456789', k=10))
    if country_code == 'FR':
        return '+33' + ''.join(random.choices('0123456789', k=9))
    if country_code == 'CN':
        return '+86' + ''.join(random.choices('0123456789', k=11))
    return '+99' + ''.join(random.choices('0123456789', k=8))

def random_bvn():
    return ''.join(random.choices('0123456789', k=11))
def random_nin():
    return ''.join(random.choices('0123456789', k=11))

def pick_region_name(region, is_diaspora=False):
    """Pick region-typical or diaspora name."""
    if region == 'NG':
        first = random.choice(nigerian_first)
        last = random.choice(nigerian_last)
    elif region == 'UK':
        if not is_diaspora:
            first = fake_uk.first_name()
            last = fake_uk.last_name()
        else:
            k = random.choice(list(diaspora_name_sets.keys()))
            first = random.choice(diaspora_name_sets[k][0])
            last = random.choice(diaspora_name_sets[k][1])
    elif region == 'US':
        if not is_diaspora:
            first = fake_us.first_name()
            last = fake_us.last_name()
        else:
            k = random.choice(list(diaspora_name_sets.keys()))
            first = random.choice(diaspora_name_sets[k][0])
            last = random.choice(diaspora_name_sets[k][1])
    elif region == 'FR':
        if not is_diaspora:
            ["compliance-bot", "audit_bot", "user01@lemfi.com", "y.wang@worldremit.com", "", None]
# Nigerian names (Yoruba, Igbo, Hausa, some dirty/corrupted)
yoruba_names = ["Adeola Adebayo", "Olamide Oyebanji", "Folake Ogunleye", "Temitope Ajayi", "Funmilayo Olaniyan", "Oluwaseun Olatunji", "Taiwo Oyetunde", "Bolaji Bankole"]
igbo_names = ["Chinedu Okeke", "Ngozi Nwachukwu", "Amarachi Eze", "Ifunanya Nwankwo", "Obinna Uzo", "Ifeoma Obi", "Chukwudi Okafor"]
hausa_names = ["Amina Bello", "Musa Abdullahi", "Fatima Suleiman", "Yakubu Sani", "Hauwa Ibrahim", "Aliyu Mohammed", "Zainab Garba"]
naija_dirty = ["ADE", "Olatunde ", "Efe..", "Chinédù@", "Bello_123", "Tunde---", "Chuks O.", "Ngozi ", "Temi!", "Femi/"]

# Diaspora names for UK/US/FR/CN
diaspora_names = [
    "Ayo Adesina", "Fatoumata Diallo", "Priya Patel", "Mohamed Ahmed", "Olga Nowak", "Rajiv Shah", "Layla Alhassan",
    "Linh Nguyen", "Blessing Chukwuma", "Kwame Mensah", "Yasmin El-Sayed", "Chiamaka Okafor", "Amina Abubakar"
]

# Regional name generators for 'majority' cases
def region_name(region):
    if region == "UK":
        return fake_uk.name()
    elif region == "US":
        return fake_us.name()
    elif region == "FR":
        return fake_fr.name()
    elif region == "CN":
        return fake_cn.name()
    else:
        return random.choice(yoruba_names + igbo_names + hausa_names + naija_dirty)

def diaspora_or_major(region):
    # 80–90% majority region-typical, 10–20% diaspora name
    if random.random() < 0.15:
        return random.choice(diaspora_names)
    else:
        return region_name(region)

# Nigerian address generator (raw, Lagos focus, dirty/partial, with regional mix)
def fake_naija_address():
    addrs = [
        "12 Allen Ave, Ikeja, Lagos", "B6 Lekki Phase 1, Lagos", "45 Ogui Rd, Enugu", "Plot 33, Aminu Kano, Kano",
        "Ring Rd, Ibadan", "No. 4, Waziri St, Abuja", "Sabon Gari, Zaria", "25 Oba Akran, Lagos", "Ojota, Lagos", 
        "Badagry - Mile 2", "Yaba/Surulere", "Port Harcourt", "Onitsha Market", "Victoria Island, L", "Oshodi—", "Asaba", "", "Sabo, Yaba"
    ]
    # Some dirty: drop city/state, add emoji, blank, typo, random extra chars
    if random.random() < 0.12:
        return random.choice(addrs)[:random.randint(7, 20)] + random.choice(["", "!!", "...", "🙂", " "])
    return random.choice(addrs)

def regional_address(region):
    if region == "UK":
        return fake_uk.address()
    elif region == "US":
        return fake_us.address()
    elif region == "FR":
        return fake_fr.address()
    elif region == "CN":
        return fake_cn.address()
    elif region == "NG":
        return fake_naija_address()
    else:
        return fake.address()

def diaspora_address(region):
    # If diaspora, may be region's address or Nigerian one, occasionally garbled
    if random.random() < 0.7:
        return regional_address(region)
    else:
        return fake_naija_address()

def random_date(start_year=2022, end_year=2026, as_datetime=True):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 1, 30)
    delta = end - start
    random_days = random.randint(0, delta.days)
    d = start + timedelta(days=random_days, hours=random.randint(0,23), minutes=random.randint(0,59))
    return d if as_datetime else d.strftime('%Y-%m-%d %H:%M:%S')

def messy_string(s, prob=0.10):
    if s is None:
        return None
    if not isinstance(s, str) or len(s) < 1:
        return s
    if random.random() < prob:
        if len(s) > 2:
            return s[:random.randint(1, len(s)-1)] + random.choice(["", ".", "💸", " ", "---", "?", "🙂"])
        else:
            return s + random.choice(["", ".", "💸", " ", "---", "?", "🙂"])
    return s


def messy_value(val, prob=0.08):
    if random.random() < prob:
        return random.choice(["", None, np.nan, "—"])
    return val

# Naija BVN/NIN
def fake_bvn():
    return str(random.randint(10000000000, 99999999999))
def fake_nin():
    return str(random.randint(10000000000, 99999999999))

def fake_phone(region):
    if region == "NG":
        base = "+234" + str(random.randint(7000000000, 9099999999))
    elif region == "UK":
        base = "+44" + str(random.randint(7000000000, 7999999999))
    elif region == "US":
        base = "+1" + str(random.randint(2000000000, 9999999999))
    elif region == "FR":
        base = "+33" + str(random.randint(600000000, 799999999))
    elif region == "CN":
        base = "+86" + str(random.randint(10000000000, 19999999999))
    else:
        base = "+999" + str(random.randint(100000000, 999999999))
    # Dirty/duplicate/invalid 10%: too short, too long, symbols, missing
    if random.random() < 0.10:
        base = base[:random.randint(5, 9)] + random.choice(["", "---", "x", "🤳", " "])
    return base

def fake_kyc():
    # 15% chance of missing/messy
    status = random.choice(kyc_status_choices)
    return messy_value(status, prob=0.12)

# =========== 1. COUNTRIES =============
countries = pd.DataFrame(country_list)
countries.to_csv("Countries.csv", index=False)

# =========== 2. CURRENCIES =============
currencies = pd.DataFrame(currency_list)
currencies.to_csv("Currencies.csv", index=False)

# =========== 3. COMPLIANCE_CHECK_TYPES =============
compliance_check_types = pd.DataFrame({
    "id": range(1, len(compliance_types)+1),
    "check_type": compliance_types
})
compliance_check_types.to_csv("Compliance_check_types.csv", index=False)

# =========== 4. CUSTOMERS =============

customer_rows = []
customer_count = random.randint(30, 80)
for i in range(customer_count):
    # Choose country of residence
    country_idx = np.random.choice(range(len(country_list)), p=[0.32, 0.24, 0.18, 0.15, 0.11]) # more NG,UK
    country_code = country_list[country_idx]['code']
    # Name logic
    if country_code == "NG":
        name = messy_string(random.choice(yoruba_names + igbo_names + hausa_names + naija_dirty), prob=0.18)
        diaspora = False
    else:
        # 80–90% region, 10–20% diaspora
        if random.random() < 0.16:
            name = messy_string(random.choice(diaspora_names), prob=0.25)
            diaspora = True
        else:
            name = messy_string(region_name(country_code), prob=0.10)
            diaspora = False
    dob = fake.date_of_birth(minimum_age=18, maximum_age=67)
    address = diaspora_address(country_code) if diaspora else regional_address(country_code)
    phone = fake_phone(country_code)
    # Only Nigerians/diaspora may have BVN/NIN
    bvn = fake_bvn() if (country_code == "NG" or diaspora) and random.random() > 0.12 else messy_value("", 0.8)
    nin = fake_nin() if (country_code == "NG" or diaspora) and random.random() > 0.13 else messy_value("", 0.82)
    kyc = fake_kyc()
    created_at = random_date(2022, 2025)
    customer_rows.append({
        "id": i+1,
        "full_name": name,
        "dob": dob,
        "address": address,
        "phone_number": messy_value(phone, 0.07),
        "bvn": bvn,
        "nin": nin,
        "country_of_residence": country_code if random.random() > 0.03 else messy_value(country_code, 0.9),
        "kyc_status": kyc,
        "created_at": created_at
    })

customers = pd.DataFrame(customer_rows)
# About 7% corrupted/incomplete: drop some addresses/names/BVN/NIN at random
for idx in customers.sample(frac=0.08, random_state=99).index:
    field = random.choice(['address', 'bvn', 'full_name', 'nin', 'phone_number'])
    customers.at[idx, field] = messy_value("", 1.0)

customers.to_csv("Customers.csv", index=False)

# =========== 5. ACCOUNTS =============
account_rows = []
account_id = 1
account_country_choices = [c['code'] for c in country_list]
for cust in customers.itertuples():
    n_acc = np.random.randint(1, 6)
    for _ in range(n_acc):
        # About 17% diaspora: assign an account in a different country
        if random.random() < 0.17:
            country_code = random.choice(account_country_choices)
        else:
            country_code = cust.country_of_residence
        acct_num = str(random.randint(10000000, 9999999999999))
        # Some messy: missing, duplicate, incomplete, inactive
        is_active = np.random.choice([True, False], p=[0.85, 0.15])
        created_at = random_date(2022, 2025)
        account_rows.append({
            "id": account_id,
            "account_number": messy_string(acct_num, prob=0.09),
            "customer_id": cust.id if random.random() > 0.06 else messy_value(cust.id, 0.9),
            "country_code": country_code if random.random() > 0.07 else messy_value(country_code, 0.8),
            "is_active": is_active,
            "created_at": created_at
        })
        account_id += 1

accounts = pd.DataFrame(account_rows)
# 5% incomplete/corrupted
for idx in accounts.sample(frac=0.05, random_state=91).index:
    field = random.choice(['account_number', 'customer_id', 'country_code'])
    accounts.at[idx, field] = messy_value("", 1.0)
accounts.to_csv("Accounts.csv", index=False)

# =========== 6. EXCHANGE_RATES ===========
exrate_rows = []
exrate_id = 1
all_ccys = [c['code'] for c in currency_list]
for _ in range(110):
    from_ccy = random.choice(all_ccys)
    to_ccy = random.choice([c for c in all_ccys if c != from_ccy])
    rate = round(np.random.uniform(0.005, 1300), 6)
    valid_from = random_date(2022, 2025)
    valid_to = valid_from + timedelta(days=random.randint(3, 90))
    # Messy/overlap/gaps: some to/fro code blank, some duplicate or dirty codes, some gaps in valid_from/valid_to
    if random.random() < 0.06:
        from_ccy = messy_value(from_ccy, 1.0)
    if random.random() < 0.06:
        to_ccy = messy_value(to_ccy, 1.0)
    exrate_rows.append({
        "id": exrate_id,
        "from_currency": from_ccy,
        "to_currency": to_ccy,
        "rate": rate,
        "valid_from": valid_from,
        "valid_to": valid_to
    })
    exrate_id += 1

exchange_rates = pd.DataFrame(exrate_rows)
exchange_rates.to_csv("Exchange_rates.csv", index=False)

# =========== 7. REMITTANCE ===========
remittance_rows = []
remittance_id = 1
for _ in range(random.randint(110, 220)):
    # Most remittance are cross-border, some within
    origin_country = random.choice([c['code'] for c in country_list])
    dest_country = random.choice([c['code'] for c in country_list if c['code'] != origin_country or random.random() < 0.11])
    status = random.choice(remittance_status_choices)
    ex_id = random.choice(exchange_rates['id'].values)
    method = random.choice(remittance_methods)
    created_at = random_date(2022, 2025)
    # Dirty/messy corridor/country/currency code
    if random.random() < 0.09:
        origin_country = messy_value(origin_country, 1.0)
    if random.random() < 0.09:
        dest_country = messy_value(dest_country, 1.0)
    remittance_rows.append({
        "id": remittance_id,
        "origin_country": origin_country,
        "destination_country": dest_country,
        "status": status,
        "exchange_rate_id": ex_id if random.random() > 0.08 else messy_value(ex_id, 0.9),
        "remittance_method": method,
        "created_at": created_at
    })
    remittance_id += 1

remittance = pd.DataFrame(remittance_rows)
remittance.to_csv("Remittance.csv", index=False)

# =========== 8. TRANSACTIONS ===========
transaction_rows = []
transaction_id = 1
for _ in range(random.randint(100, 500)):
    amount = round(random.choice([
        np.random.uniform(0.0, 20000),   # normal
        0.0,                            # zero edge
        -1 * np.random.uniform(0, 1000) # negative edge
    ]), 2)
    currency = random.choice(all_ccys)
    payee_id = random.choice(accounts['id'].values)
    payer_id = random.choice(accounts['id'].values)
    transaction_date = random_date(2022, 2025)
    status = random.choice(transaction_status_choices)
    is_complete = status == "SUCCESS"
    created_at = transaction_date - timedelta(minutes=random.randint(0, 7200))
    updated_at = transaction_date + timedelta(minutes=random.randint(0, 8000))
    rem_id = random.choice(remittance['id'].values)
    ex_id = random.choice(exchange_rates['id'].values)
    # Dirty/duplicate: some missing/mismatched FKs, batch, out-of-order, duplicate
    if random.random() < 0.07:
        payee_id = messy_value(payee_id, 1.0)
    if random.random() < 0.07:
        payer_id = messy_value(payer_id, 1.0)
    if random.random() < 0.07:
        rem_id = messy_value(rem_id, 1.0)
    if random.random() < 0.07:
        ex_id = messy_value(ex_id, 1.0)
    transaction_rows.append({
        "id": transaction_id,
        "amount": amount,
        "currency": messy_value(currency, 0.06),
        "payee_id": payee_id,
        "payer_id": payer_id,
        "transaction_date": transaction_date,
        "status": status,
        "is_complete": is_complete,
        "created_at": created_at,
        "updated_at": updated_at,
        "remittance_id": rem_id,
        "exchange_rate_id": ex_id
    })
    # 4% duplicate/batch
    if random.random() < 0.04:
        transaction_rows.append({
            "id": transaction_id+10000,
            "amount": amount,
            "currency": currency,
            "payee_id": payee_id,
            "payer_id": payer_id,
            "transaction_date": transaction_date,
            "status": status,
            "is_complete": is_complete,
            "created_at": created_at,
            "updated_at": updated_at,
            "remittance_id": rem_id,
            "exchange_rate_id": ex_id
        })
    transaction_id += 1

transactions = pd.DataFrame(transaction_rows)
transactions.to_csv("Transactions.csv", index=False)

# =========== 9. COMPLIANCE_CHECKS ===========
check_rows = []
check_id = 1
for tx in transactions.sample(frac=0.82, random_state=45).itertuples():
    n_checks = np.random.choice([1, 2, 3], p=[0.7, 0.22, 0.08])
    used_types = np.random.choice(compliance_check_types['id'].values, n_checks, replace=False)
    for t in used_types:
        note = random.choice(compliance_notes)
        officer = random.choice(officer_names)
        checked_at = tx.transaction_date + timedelta(minutes=random.randint(-4000, 6000))
        check_rows.append({
            "id": check_id,
            "transaction_id": tx.id if random.random() > 0.06 else messy_value(tx.id, 0.92),
            "check_type_id": t,
            "passed": np.random.choice([True, False], p=[0.89, 0.11]) if random.random() > 0.09 else messy_value(None, 0.82),
            "checked_at": checked_at,
            "notes": messy_string(note, prob=0.22),
            "checked_by": messy_string(officer, prob=0.12)
        })
        check_id += 1

compliance_checks = pd.DataFrame(check_rows)
compliance_checks.to_csv("Compliance_checks.csv", index=False)