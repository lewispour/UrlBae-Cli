import argparse
from api_client import (
    list_urls, get_single_url_details, delete_url, upload_file, 
    create_short_url, list_files, list_qr_codes, create_qr_code, 
    update_qr_code, delete_qr_code
)
from tabulate import tabulate 

def main():
    parser = argparse.ArgumentParser(description="URLbae CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    parser_ls = subparsers.add_parser('ls', help='List or get details of URLs')
    parser_ls.add_argument('--limit', type=int, default=10, help='Number of URLs to list')
    parser_ls.add_argument('--page', type=int, default=1, help='Page number')
    parser_ls.add_argument('--order', default='date', choices=['date', 'other'], help='Order of URLs')
    parser_ls.add_argument('url_id', nargs='?', help='ID of the URLbae URL to get details for')

    parser_rm = subparsers.add_parser('rm', help='Delete a URL')
    parser_rm.add_argument('url_id', help='ID of the URLbae URL to delete')

    
    # Creating a parent parser for 'files' command
    parser_files = subparsers.add_parser('files', help='Operations related to files')
    files_subparsers = parser_files.add_subparsers(dest="files_command")

    # 'ls' subcommand under 'files'
    parser_files_ls = files_subparsers.add_parser('ls', help='List files')
    parser_files_ls.add_argument('--name', help='Search for a file by name')
    parser_files_ls.add_argument('--limit', type=int, default=10, help='Number of files to list per page')
    parser_files_ls.add_argument('--page', type=int, default=1, help='Page number to display')

    # 'cp' subcommand under 'files'
    parser_files_cp = files_subparsers.add_parser('cp', help='Copy file to URLbae')
    parser_files_cp.add_argument('filename', help='Filename for the upload')
    parser_files_cp.add_argument('--name', help='File name')
    parser_files_cp.add_argument('--custom', help='Custom alias')
    parser_files_cp.add_argument('--domain', help='Custom Domain')
    parser_files_cp.add_argument('--password', help='Password protection')
    parser_files_cp.add_argument('--expiry', help='Expiration for the download')
    parser_files_cp.add_argument('--maxdownloads', type=int, help='Maximum number of downloads')

    parser_shorten = subparsers.add_parser('shorten', help='Create a new short URL')
    parser_shorten.add_argument('url', help='Long URL to shorten')
    parser_shorten.add_argument('--custom', help='Custom alias')
    parser_shorten.add_argument('--type', choices=['direct', 'frame', 'splash'], help='Redirection type')
    parser_shorten.add_argument('--password', help='Password protection')
    
    parser_qr = subparsers.add_parser('qr', help='Operations related to QR codes')
    qr_subparsers = parser_qr.add_subparsers(dest="qr_command")

    # 'ls' subcommand under 'qr'
    parser_qr_ls = qr_subparsers.add_parser('ls', help='List QR codes')
    parser_qr_ls.add_argument('--limit', type=int, default=10, help='Number of QR codes to list per page')
    parser_qr_ls.add_argument('--page', type=int, default=1, help='Page number to display')

    # 'create' subcommand under 'qr'
    parser_qr_create = qr_subparsers.add_parser('create', help='Create a QR code')
    parser_qr_create.add_argument('type', help='Type of QR code (text, vcard, link, email, phone, sms, wifi)')
    parser_qr_create.add_argument('data', help='Data to be embedded inside the QR code')
    parser_qr_create.add_argument('--background', help='RGB color for background')
    parser_qr_create.add_argument('--foreground', help='RGB color for foreground')
    parser_qr_create.add_argument('--logo', help='Path to the logo')

    # 'update' subcommand under 'qr'
    parser_qr_update = qr_subparsers.add_parser('update', help='Update a QR code')
    parser_qr_update.add_argument('qr_id', help='ID of the QR code to update')
    parser_qr_update.add_argument('data', help='Data to be embedded inside the QR code')
    parser_qr_update.add_argument('--background', help='RGB color for background')
    parser_qr_update.add_argument('--foreground', help='RGB color for foreground')
    parser_qr_update.add_argument('--logo', help='Path to the logo')

    # 'delete' subcommand under 'qr'
    parser_qr_delete = qr_subparsers.add_parser('delete', help='Delete a QR code')
    parser_qr_delete.add_argument('qr_id', help='ID of the QR code to delete')

    args = parser.parse_args()

    if args.command == 'ls':
        if args.url_id:
            print(get_single_url_details(args.url_id))
        else:
            print(list_urls(args.limit, args.page, args.order))
    elif args.command == 'rm':
        print(delete_url(args.url_id))
    elif args.command == 'files':
        if args.files_command == 'ls':
            file_list = list_files(limit=args.limit, page=args.page, name=args.name)
            print(file_list)
        elif args.files_command == 'cp':
            response = upload_file(args.filename, name=args.name, custom=args.custom, domain=args.domain, password=args.password, expiry=args.expiry, maxdownloads=args.maxdownloads)
            if not response.get('error'):
                # Extract the ID from the response
                file_id = response.get('1')  # Using the key '1' to get the ID

                # Create a list of dictionaries for tabulate
                data = [{
                    'ID': file_id,
                    'Short URL': response.get('shorturl')
                }]
                # Print the table
                print(tabulate(data, headers='keys', tablefmt='pretty'))
            else:
                print("Error occurred during file upload.")
    elif args.command == 'shorten':
        response = create_short_url(args.url, custom=args.custom, type=args.type, password=args.password)
        print("Short URL created:", response)
    elif args.command == 'qr':
            if args.qr_command == 'ls':
                qr_list = list_qr_codes(limit=args.limit, page=args.page)
                print(qr_list)
            elif args.qr_command == 'create':
                response = create_qr_code(args.type, args.data, background=args.background, foreground=args.foreground, logo=args.logo)
                print(response)
            elif args.qr_command == 'update':
                response = update_qr_code(args.qr_id, args.data, background=args.background, foreground=args.foreground, logo=args.logo)
                print(response)
            elif args.qr_command == 'delete':
                response = delete_qr_code(args.qr_id)
                print(response)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
