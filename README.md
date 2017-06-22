# Nmap-ssl-parser 

Nmap-ssl-parser is a python script designed to query nmap XML output and provide a list of usable ssl services in the format `host:port`

The nmap-ssl-parser script parses an nmap.xml output file, extracts all SSL services and writes them to a file.

## Installation

git clone https://github.com/attackdebris/nmap-ssl-parser.git

### Prerequisites 

The only pre-reqs is:

1. You need a valid Nmap XML output file (see below)

### Nmap XML File

The Nmap XML file must have been created with version scanning enabled i.e. via Nmap flags `-sV` or `-A` (see below) 

```bash
nmap -A -p 1-65535 -iL targets.txt -oX nmap-output.xml 
nmap -sS -sV -p 1-65535 -iL targets.txt -oX nmap-output.xml
```

## Usage

```bash
./nmap-ssl-parser.py 
nmap-ssl-parser - v0.2 ( https://github.com/attackdebris/nmap-ssl-parser )

USAGE: nmap-ssl-parser.py [nmap-ouput.xml] [outputfile]
```

### Example
```bash
./nmap-ssl-parser.py nmap-output.xml ssl-services.txt
nmap-ssl-parser - v0.2 ( https://github.com/attackdebris/nmap-ssl-parser )

Results saved to: ssl-services.txt
```

### Output / Results

The output from the script is concatenated file (see below)

```bash
cat ssl-services.txt 

185.176.90.16:443
199.101.100.186:31337
```
