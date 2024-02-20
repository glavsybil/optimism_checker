def read_eligible_list(file_path):
    eligible_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            address, summ = line.strip().split(',')
            eligible_dict[address] = float(summ)
    return eligible_dict

def read_wallets(file_path):
    wallets = []
    with open(file_path, 'r') as file:
        for line in file:
            wallets.append(line.strip())
    return wallets

def check_address(eligible_dict, address):
    address=address.lower()
    if address in eligible_dict:
        return eligible_dict[address]
    else:
        return 0

if __name__ == "__main__":
    eligible_dict = read_eligible_list("eligible.txt")
    wallets = read_wallets("wallets.txt")
    total_drop=0
    for address in wallets:
        summ = check_address(eligible_dict, address)
        total_drop+=summ
        print(f"Address: {address}, op: {summ}")
    print(f'Total airdrop: {total_drop}')