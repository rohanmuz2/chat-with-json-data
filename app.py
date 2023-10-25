# Test on some sample data
json_value = {
   "entity":{
      "Entity Name":"BAYLIS & HARDING PUBLIC LIMITED COMPANY",
      "bvdId":"GB01389887",
      "Country":"GB",
      "runDetails":{
         "searchRequestID":"9c269fb4-dd9d-40d3-a956-b18078ed71d5J13RP",
         "status":"processedWithoutException",
         "runDateTime":"2023-08-10T15:55:17.122827"
      },
      "targetEntity":{
         "organisation":{
            "legalName":{
               "value":"BAYLIS & HARDING PUBLIC LIMITED COMPANY",
               "dataSource":"BvD"
            },
            "localName":{
               "value":"BAYLIS & HARDING PUBLIC LIMITED COMPANY",
               "dataSource":"BvD"
            },
            "countryofIncorporation":{
               "value":"GB",
               "dataSource":"BvD"
            },
            "incorporationDate":{
               "value":"1978-09-19",
               "dataSource":"BvD"
            },
            "entityType":{
               "value":"Corporate",
               "dataSource":"BvD"
            },
            "legalForm":{
               "value":"Public limited companies",
               "dataSource":"BvD"
            },
            "financialDetails":[
               {
                  "accountsDate":{
                     "value":"2022-05-31",
                     "dataSource":"BvD"
                  },
                  "currency":{
                     "value":"GBP",
                     "dataSource":"BvD"
                  },
                  "numberOfEmployees":{
                     "value":"86",
                     "dataSource":"BvD"
                  },
                  "totalAssets":{
                     "value":"24968678",
                     "dataSource":"BvD"
                  },
                  "operationalRevenue":{
                     "value":"55340686",
                     "dataSource":"BvD"
                  },
                  "profitAfterTax":{
                     "value":"2738766",
                     "dataSource":"BvD"
                  },
                  "currentLiability":{
                     "value":"5177599",
                     "dataSource":"BvD"
                  },
                  "totalAssetsUSD":{
                     "value":"31433078.820957661",
                     "dataSource":"BvD"
                  },
                  "operationalRevenueUSD":{
                     "value":"69668411.961733341",
                     "dataSource":"BvD"
                  },
                  "patUSD":{
                     "value":"3447833.62379694",
                     "dataSource":"BvD"
                  },
                  "currentLiabilitiesUSD":{
                     "value":"6518081.472728014",
                     "dataSource":"BvD"
                  }
               },
               {
                  "accountsDate":{
                     "value":"2021-05-31",
                     "dataSource":"BvD"
                  },
                  "currency":{
                     "value":"GBP",
                     "dataSource":"BvD"
                  },
                  "numberOfEmployees":{
                     "value":"80",
                     "dataSource":"BvD"
                  },
                  "totalAssets":{
                     "value":"26955723",
                     "dataSource":"BvD"
                  },
                  "operationalRevenue":{
                     "value":"60222399",
                     "dataSource":"BvD"
                  },
                  "profitAfterTax":{
                     "value":"4200391",
                     "dataSource":"BvD"
                  },
                  "currentLiability":{
                     "value":"7864253",
                     "dataSource":"BvD"
                  },
                  "totalAssetsUSD":{
                     "value":"38074936.8865664",
                     "dataSource":"BvD"
                  },
                  "operationalRevenueUSD":{
                     "value":"85064089.769828081",
                     "dataSource":"BvD"
                  },
                  "patUSD":{
                     "value":"5933048.8825657368",
                     "dataSource":"BvD"
                  },
                  "currentLiabilitiesUSD":{
                     "value":"11108250.987554312",
                     "dataSource":"BvD"
                  }
               }
            ],
            "stockExchange":[
               {
                  "tradingStatus":{
                     "value":"Unlisted",
                     "dataSource":"BvD"
                  }
               }
            ],
            "address":[
               {
                  "type":{
                     "value":"Registered Address",
                     "dataSource":"BvD"
                  },
                  "addressLine1":{
                     "value":"THE I O CENTRE",
                     "dataSource":"BvD"
                  },
                  "addressLine2":{
                     "value":"NASH ROAD, PARK FARM",
                     "dataSource":"BvD"
                  },
                  "city":{
                     "value":"REDDITCH",
                     "dataSource":"BvD"
                  },
                  "countryName":{
                     "value":"United Kingdom",
                     "dataSource":"BvD"
                  },
                  "country":{
                     "value":"GB",
                     "dataSource":"BvD"
                  },
                  "postCode":{
                     "value":"B98 7AS",
                     "dataSource":"BvD"
                  }
               }
            ],
            "industry":[
               {
                  "type":{
                     "value":"SIC (US 1987)",
                     "dataSource":"BvD"
                  },
                  "industryCode":{
                     "value":"2841",
                     "dataSource":"BvD"
                  },
                  "description":{
                     "value":"Soap and Other Detergents, Except Specialty Cleaners",
                     "dataSource":"BvD"
                  }
               },
               {
                  "type":{
                     "value":"SIC (US 1987)",
                     "dataSource":"BvD"
                  },
                  "industryCode":{
                     "value":"2844",
                     "dataSource":"BvD"
                  },
                  "description":{
                     "value":"Perfumes, Cosmetics, and Other Toilet Preparations",
                     "dataSource":"BvD"
                  }
               }
            ]
         }
      }
   }
}


# JSON Schema object that the above JSON value conforms to
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "entity": {
            "type": "object",
            "properties": {
                "Entity Name": {
                    "type": "string"
                },
                "bvdId": {
                    "type": "string"
                },
                "Country": {
                    "type": "string"
                },
                "runDetails": {
                    "type": "object",
                    "properties": {
                        "searchRequestID": {
                            "type": "string"
                        },
                        "status": {
                            "type": "string"
                        },
                        "runDateTime": {
                            "type": "string",
                            "format": "date-time"
                        }
                    },
                    "required": ["searchRequestID", "status", "runDateTime"]
                },
                "targetEntity": {
                    "type": "object",
                    "properties": {
                        "organisation": {
                            "type": "object",
                            "properties": {
                                "legalName": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "localName": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "countryofIncorporation": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "incorporationDate": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "entityType": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "legalForm": {
                                    "$ref": "#/definitions/nameDataSource"
                                },
                                "financialDetails": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/financialDetail"
                                    }
                                },
                                "stockExchange": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "tradingStatus": {
                                                "$ref": "#/definitions/nameDataSource"
                                            }
                                        },
                                        "required": ["tradingStatus"]
                                    }
                                },
                                "address": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/addressDetail"
                                    }
                                },
                                "industry": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/industryDetail"
                                    }
                                }
                            },
                            "required": [
                                "legalName", "localName", "countryofIncorporation", "incorporationDate", "entityType", "legalForm", "financialDetails", "stockExchange", "address", "industry"
                            ]
                        }
                    },
                    "required": ["organisation"]
                }
            },
            "required": ["Entity Name", "bvdId", "Country", "runDetails", "targetEntity"]
        }
    },
    "required": ["entity"],
    "definitions": {
        "nameDataSource": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string"
                },
                "dataSource": {
                    "type": "string"
                }
            },
            "required": ["value", "dataSource"]
        },
        "financialDetail": {
            "type": "object",
            "properties": {
                "accountsDate": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "currency": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "numberOfEmployees": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "totalAssets": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "operationalRevenue": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "profitAfterTax": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "currentLiability": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "totalAssetsUSD": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "operationalRevenueUSD": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "patUSD": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "currentLiabilitiesUSD": {
                    "$ref": "#/definitions/nameDataSource"
                }
            }
        },
        "addressDetail": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "addressLine1": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "addressLine2": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "city": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "countryName": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "country": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "postCode": {
                    "$ref": "#/definitions/nameDataSource"
                }
            },
            "required": ["type", "addressLine1", "city", "countryName", "country", "postCode"]
        },
        "industryDetail": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "industryCode": {
                    "$ref": "#/definitions/nameDataSource"
                },
                "description": {
                    "$ref": "#/definitions/nameDataSource"
                }
            },
            "required": ["type", "industryCode", "description"]
        }
    }
}

from sys import displayhook
from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.indices.struct_store import JSONQueryEngine



llm = OpenAI(model="gpt-4")
service_context = ServiceContext.from_defaults(llm=llm)
nl_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
)
raw_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
    synthesize_response=False,
)

# nl_response = nl_query_engine.query(
#     "What is the address of COMPANY?",
# )
# raw_response = raw_query_engine.query(
#     "What is the address of COMPANY?",
# )

# nl_response = nl_query_engine.query(
#     "What is registered country of company?",
# )
# raw_response = raw_query_engine.query(
#     "What is registered country of company?",
# )


# nl_response = nl_query_engine.query(
#     "Is this company listed on stock exchange?",
# )
# raw_response = raw_query_engine.query(
#     "Is this company listed on stock exchange?",
# )

nl_response = nl_query_engine.query(
    "What is incorporation date of company",
)
raw_response = raw_query_engine.query(
    "What is incorporation date of company",
)

print("===========")
print(nl_response)

print("============")
print(raw_response)