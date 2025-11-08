# Demand Adder

Demand Adder is a tool to add demand to Subway Builder maps.

## Installation

Download Python from https://www.python.org/downloads/ if not already installed.

Then, download the .py file from here.

Install it into the folder that has the demand_data.json file you wish to edit. (On Windows it should be something like C:\Users\Sam\AppData\Local\Programs\Subway Builder\resources\data\\[CITY CODE]\demand_data)

## Usage

Run the script from the same folder as the demand_data.json you wish to edit.

The script asks for a residence id and a work id. You can find these by opening the demand_data.json and finding which ids correspond to in game demand bubbles. I often ctrl + f and look for demand bubbles that have the same amount of residents/jobs.

Once you find where you want residents and where you want workers, the script asks how much demand you wish to add. Any number should work.

## Limitations

This script was made very quick and dirty to demonstrate what is possible, so at the moment there are two main drawbacks.

The script must be in the same folder as the demand_data.json and additional demand is point to point, not spread across an area. 

This means that if I wanted to model for example the significant cross-border traffic in San Diego with a border demand bubble, I would have to manually assign every single commute.

## Contributing

This script is super simplistic and more a proof of concept. I would love to see how you guys can improve it!
