<h1 align="center">URLbae CLI Tool</h1>

<p align="center">
  <img src="https://img.shields.io/github/license/lewispour/urlbae-cli" />
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/Tabulate-0.9.0+-blue.svg" />



URLbae CLI Tool is an advanced command-line application for managing URLs, files, and QR codes using the URLbae API. It provides a straightforward and efficient way to shorten URLs, manage files, and create or manipulate QR codes directly from the terminal.

</p>

## Features

- URL Shortening: Easily shorten URLs with custom alias, redirection type, and password protection.
- File Management: Upload, list, and delete files stored in URLbae.
- QR Code Operations: Create, list, update, and delete QR codes.

## Installation

# Clone the repository
```git clone https://github.com/lewispour/urlbae-cli.git```

# Navigate to the cloned directory
```cd UrlBae-Cli```

# Install required packages
```pip install -r requirements.txt```

## Usage
## Default Usage Without Parameters

URLbae CLI is designed for ease of use, providing straightforward command-line options. Here’s how to use its various features in their default modes:

### URL Operations

- **List URLs (Default Settings)**: Lists the first 10 URLs, ordered by date.
```
  python urlbae-cli.py ls
```

- **Get Single URL Details**: Retrieve details of a specific URL by its ID.
```
  python urlbae-cli.py ls [url_id]
```

- **Delete a URL**: Remove a specific URL using its ID.
```
  python urlbae-cli.py rm [url_id]
```

- **Create Short URL (Default Settings)**: Create a shortened URL without custom options.
```
  python urlbae-cli.py shorten [long_url]
```

### File Operations

- **List Files (Default Settings)**: Displays the first 10 files.
```
  python urlbae-cli.py files ls
```

- **Upload a File**: Upload a file with default settings.
```
  python urlbae-cli.py files cp [filename]
```

### QR Code Operations

- **List QR Codes (Default Settings)**: Shows the first 10 QR codes.
```
  python urlbae-cli.py qr ls
```

- **Create a QR Code (Default Settings)**: Generate a QR code with default parameters.
```
  python urlbae-cli.py qr create [type] [data]
```

- **Update a QR Code**: Modify an existing QR code by its ID.
```
  python urlbae-cli.py qr update [qr_id] [data]
```

- **Delete a QR Code**: Remove a QR code using its ID.
```
  python urlbae-cli.py qr delete [qr_id]
```
## **_Using the Help Command_**

**_Note:_** At any point, you can use the `-h` or `--help` flag with any command or subcommand to get detailed information about its usage and available parameters. This feature is incredibly helpful for understanding the functionality and options of each command within the URLbae CLI tool.

For example:
```
  python urlbae-cli.py -h
```
```
  python urlbae-cli.py ls -h
```
```
  python urlbae-cli.py files cp -h
```
```
  python urlbae-cli.py qr create -h
```

## Parameterized Usage

URLbae CLI offers various command options to cater to specific needs. Below are examples of how to use these commands with their available parameters:

### URL Operations

- **List URLs with Parameters**: List URLs with custom limits, pages, and order.
```
  python urlbae-cli.py ls --limit [number] --page [number] --order [date/other]
```
  - `--limit`: Number of URLs to list (default is 10).
  - `--page`: Page number for pagination.
  - `--order`: Order of URLs, can be 'date' or other criteria.

- **Get Single URL Details**: Retrieve details of a specific URL by its ID.
```
  python urlbae-cli.py ls [url_id]
```

- **Delete a URL**: Remove a specific URL using its ID.
```
  python urlbae-cli.py rm [url_id]
```

- **Create Short URL with Parameters**: Create a shortened URL with additional options.
```
  python urlbae-cli.py shorten [long_url] --custom [alias] --type [direct/frame/splash] --password [password]
```
  - `--custom`: Custom alias for the shortened URL.
  - `--type`: Type of redirection (direct, frame, or splash).
  - `--password`: Password to protect the URL.

### File Operations

- **List Files with Parameters**: Display files with custom limits and pages.
```
  python urlbae-cli.py files ls --limit [number] --page [number] --name [filename]
```
  - `--limit`: Number of files to list per page.
  - `--page`: Page number for pagination.
  - `--name`: Search for a file by name.

- **Upload a File with Parameters**: Upload a file with custom options.
```
  python urlbae-cli.py files cp [filename] --name [display_name] --custom [alias] --domain [domain] --password [password] --expiry [date] --maxdownloads [number]
```
  - `--name`: Display name for the file.
  - `--custom`: Custom alias for the file URL.
  - `--domain`: Custom domain for the file URL.
  - `--password`: Password to protect the file.
  - `--expiry`: Expiration date for the download link.
  - `--maxdownloads`: Maximum number of downloads allowed.

### QR Code Operations

- **List QR Codes with Parameters**: Show QR codes with custom limits and pages.
```
  python urlbae-cli.py qr ls --limit [number] --page [number]
```
  - `--limit`: Number of QR codes to list per page.
  - `--page`: Page number for pagination.

- **Create a QR Code with Parameters**: Generate a QR code with additional options.
```
  python urlbae-cli.py qr create [type] [data] --background [color] --foreground [color] --logo [url]
```
  - `--background`: RGB color for the QR code background.
  - `--foreground`: RGB color for the QR code foreground.
  - `--logo`: URL to a logo image to be included in the QR code.

- **Update a QR Code with Parameters**: Modify an existing QR code.
```
  python urlbae-cli.py qr update [qr_id] [data] --background [color] --foreground [color] --logo [url]
```

- **Delete a QR Code**: Remove a QR code using its ID.
```
  python urlbae-cli.py qr delete [qr_id]
```




## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (```git checkout -b feature/AmazingFeature```)
3. Commit your Changes (```git commit -m 'Add some AmazingFeature'```)
4. Push to the Branch (```git push origin feature/AmazingFeature```)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Useful Link: [UrlBae API Documentation](https://urlbae.com/developers)
- Project Link: [https://github.com/lewispour/urlbae-cli](https://github.com/lewispour/urlbae-cli)
