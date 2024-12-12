interface Tester {
  name: string;
  id: number;
  callback(): void;
}

const test: Tester = {
  name: "Andrew",
  id: 3042,
  callback() {
    console.log(`${this.name} with id of ${this.id}`);
  },
};

test.callback();

interface Dictionary<> {
  [key: string]: number;
}

const dict: Dictionary = {};

dict["first"] = 0;
dict["first"] = 1;
console.log(dict);

import axios from "axios";
import * as cheerio from "cheerio";

async function scrapeData(url: string): Promise<string[]> {
  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    const data: string[] = [];

    $("h1").each((index, element) => {
      data.push($(element).text());
    });

    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

scrapeData("https://example.com").then((data) => console.log(data));
