import argparse


from getcontact.getcontact import GetContactAPI


description = 'Get infomation about phone number from databases of GetContact App'

parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-p', '--phone', help='Phone number (example: +78005553535)')
parser.add_argument('-j', '--json', help='Print output in JSON format', action='store_true')
parser.add_argument('-m', '--max_name', help='Print maximum matching names', action='store_true')
args = parser.parse_args()

phone = args.phone
getcontact = GetContactAPI()

if args.

if args.json:
    print(getcontact.get_information_by_phone(phone))
else:
    getcontact.print_information_by_phone(phone)
