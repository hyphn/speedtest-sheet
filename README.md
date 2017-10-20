# speedtest-sheet

[![MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/jakeoid/waste-basket/blob/master/LICENSE.md)

Logs your internet speeds to a spreadsheet so you can complete whatever with it!

## Installation

Note that installation will require a Google Developers account & application. Information on how to create such an application can be found here, note that you only need to get the credits.json file!

#### 1. Install requirements.

```sh
pip3.6 install -r ./requirements.txt
```

#### 2. Create a configuration files.
```sh
cp config.template.json config.json
cp credits.template.json credits.json
```

#### 3. Edit configuration file information.
```sh
nano config.json credits.json
```

#### 4. Run the script and profit!
```sh
python3.6 app.py
```

## License

See `LICENSE.md` for details on that.