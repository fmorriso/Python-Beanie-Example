import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

'''
{
  "count": 16,
  "fields": [
    {
      "name": "_id",
      "path": [
        "_id"
      ],
      "count": 16,
      "type": "ObjectId",
      "probability": 1,
      "hasDuplicates": false,
      "types": [
        {
          "name": "ObjectId",
          "path": [
            "_id"
          ],
          "count": 16,
          "probability": 1,
          "unique": 16,
          "hasDuplicates": false,
          "values": [
            "6631212e476efa50bd891b0f",
            "6631212e476efa50bd891b1c",
            "6631212e476efa50bd891b17",
            "6631212e476efa50bd891b10",
            "6631212e476efa50bd891b12",
            "6631212e476efa50bd891b1a",
            "6631212e476efa50bd891b1b",
            "6631212e476efa50bd891b15",
            "6631212e476efa50bd891b16",
            "6631212e476efa50bd891b14",
            "6631212e476efa50bd891b18",
            "6631212e476efa50bd891b13",
            "6631212e476efa50bd891b0e",
            "6631212e476efa50bd891b1d",
            "6631212e476efa50bd891b11",
            "6631212e476efa50bd891b19"
          ],
          "bsonType": "ObjectId"
        }
      ]
    },
    {
      "name": "category",
      "path": [
        "category"
      ],
      "count": 16,
      "type": "String",
      "probability": 1,
      "hasDuplicates": true,
      "types": [
        {
          "name": "String",
          "path": [
            "category"
          ],
          "count": 16,
          "probability": 1,
          "unique": 6,
          "hasDuplicates": true,
          "values": [
            "Sweater",
            "T-Shirt",
            "T-Shirt",
            "Mask",
            "T-Shirt",
            "T-Shirt",
            "Jacket",
            "T-Shirt",
            "Hat",
            "T-Shirt",
            "T-Shirt",
            "Hoodie",
            "Hoodie",
            "T-Shirt",
            "T-Shirt",
            "T-Shirt"
          ],
          "bsonType": "String"
        }
      ]
    },
    {
      "name": "id",
      "path": [
        "id"
      ],
      "count": 16,
      "type": "Int32",
      "probability": 1,
      "hasDuplicates": false,
      "types": [
        {
          "name": "Int32",
          "path": [
            "id"
          ],
          "count": 16,
          "probability": 1,
          "unique": 16,
          "hasDuplicates": false,
          "values": [
            2,
            15,
            10,
            3,
            5,
            13,
            14,
            8,
            9,
            7,
            11,
            6,
            1,
            16,
            4,
            12
          ],
          "bsonType": "Int32"
        }
      ]
    },
    {
      "name": "image",
      "path": [
        "image"
      ],
      "count": 16,
      "type": "String",
      "probability": 1,
      "hasDuplicates": false,
      "types": [
        {
          "name": "String",
          "path": [
            "image"
          ],
          "count": 16,
          "probability": 1,
          "unique": 16,
          "hasDuplicates": false,
          "values": [
            "/images/css.jpg",
            "/images/vscode.jpg",
            "/images/python.jpg",
            "/images/github.jpg",
            "/images/java.jpg",
            "/images/vite.jpg",
            "/images/tailwind.jpg",
            "/images/node.js.jpg",
            "/images/npm.jpg",
            "/images/mongodb.png",
            "/images/react.jpg",
            "/images/javascript.jpg",
            "/images/cplusplus.jpg",
            "/images/vue.jpg",
            "/images/html.jpg",
            "/images/angular.jpg"
          ],
          "bsonType": "String"
        }
      ]
    },
    {
      "name": "name",
      "path": [
        "name"
      ],
      "count": 16,
      "type": "String",
      "probability": 1,
      "hasDuplicates": false,
      "types": [
        {
          "name": "String",
          "path": [
            "name"
          ],
          "count": 16,
          "probability": 1,
          "unique": 16,
          "hasDuplicates": false,
          "values": [
            "CSS Sweater",
            "VS Code T-Shirt",
            "Python T-Shirt",
            "GitHub Mask",
            "Java T-Shirt",
            "Vite T-Shirt",
            "TailwindCSS Jacket",
            "Node.js T-Shirt",
            "npm Hat",
            "MongoDB T-Shirt",
            "React T-Shirt",
            "JavaScript Hoodie",
            "C++ Hoodie",
            "Vue T-Shirt",
            "HTML T-Shirt",
            "Angular T-Shirt"
          ],
          "bsonType": "String"
        }
      ]
    },
    {
      "name": "price",
      "path": [
        "price"
      ],
      "count": 16,
      "type": "Int32",
      "probability": 1,
      "hasDuplicates": true,
      "types": [
        {
          "name": "Int32",
          "path": [
            "price"
          ],
          "count": 16,
          "probability": 1,
          "unique": 4,
          "hasDuplicates": true,
          "values": [
            49,
            39,
            39,
            19,
            39,
            39,
            39,
            39,
            29,
            39,
            39,
            49,
            49,
            39,
            39,
            39
          ],
          "bsonType": "Int32"
        }
      ]
    }
  ]
}
'''


class Products(BaseModel):
    category: str
    name: str
    price: float
    image: str

    class Settings:
        name = 'products'
