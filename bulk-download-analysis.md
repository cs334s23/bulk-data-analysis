
# Regulations.gov Bulk Data vs API

&nbsp;&nbsp;&nbsp;&nbsp;The data in the csv is organized completely flat in rows,
since that is the only form the CSV format offers.
Each row represents a document and has a unique document id
stored in the "Document ID" column.
Regarding the system as a whole, comments are considered as
documents and have their own document id.
This is how comments are stored in the csv, on separate
rows along with each document.

&nbsp;&nbsp;&nbsp;&nbsp;The Documents API and the Comments API jointly provide
most of the fields that are contained in the bulk CSV data. Every comment
can be requested from the documents API as well since every comment
is a document.

## API Response JSON for both the Document API and the Comment API
`

	"data": {
		"id": "CMS-2022-0113-1871" (Document ID),
		"type": either "documents" or "comments",
		"links": {
			"self": "https://api.regulations.gov/v4/documents/CMS-2022-0113-1871"
		},
		"attributes": {
			"authors": null,
			...
			"topics": [
				"Administrative Practices and Procedures",
				"Health Facilities",
				...
			],
			"displayProperties": [
				{
					"name": "pageCount",
					"label": "Page Count",
					"tooltip": "Number of pages In the content file"
				}
			],
			"fileFormats": [
				{
					"fileUrl": "https://downloads.regulations.gov/CMS-2022-0113-1871/content.pdf",
					"format": "pdf",
					"size": 40338878
				},
				{
					"fileUrl": "https://downloads.regulations.gov/CMS-2022-0113-1871/content.htm",
					"format": "htm",
					"size": 3492491
				}
			]
		},
		"relationships": {
			"attachments": {
				"data": [
					{
						"id": "09000064851f89b5",
						"type": "attachments"
					}
				],
				"links": {
					"self": "https://api.regulations.gov/v4/documents/CMS-2022-0113-1871/relationships/attachments",
					"related": "https://api.regulations.gov/v4/documents/CMS-2022-0113-1871/attachments"
				}
			}
		}
	},
	"included": [
		{
			"id": "09000064851f89b5",
			"type": "attachments",
			"links": {
				"self": "https://api.regulations.gov/v4/attachments/09000064851f89b5"
			},
			"attributes": {
				"authors": null,
				...
				"fileFormats": [
					{
						"fileUrl": "https://downloads.regulations.gov/CMS-2022-0113-1871/attachment_1.pdf",
						"format": "pdf",
						"size": 63315952
					}
				]
			}
		}
	]
`

## CSV vs JSON Comparisons by Field

&nbsp;&nbsp;&nbsp;&nbsp;There are fields that are
common to all sources but every source has at least one field
not contained in the other sources. Listed below are the different
field combinations.
"FR Citation" and "frVolNum" are the only two fields
of interest that are missing in the bulk data or the
APIs. All other fields are either not important or can be
found in the CSV bulk data and at least one of the APIs.

**Total Number Of Unique Fields: 70**


### Fields Present In All (37)
| CSV Field Name | Documents API Field Name | Comments API Field Name |
| --- | --- | --- |
| Abstract | docAbstract | docAbstract |
| Additional Field 1 | field1 | field1 |
| Additional Field 2 | field2 | field2 |
| Agency ID | agencyId | agencyId |
| Attachment Files<sup>1</sup> | see<sup>2</sup> | see<sup>3</sup> |
| Category | category | category |
| City | city | city |
| Comment | comment | comment |
| Content Files<sup>4</sup> | fileFormats<sup>5</sup> | fileFormats<sup>5</sup> |
| Country | country | country |
| Display Properties (Name, Label, Tooltip) | displayProperties | displayProperties |
| Docket ID | docketId | docketId |
| Document ID | originalDocumentId | originalDocumentId<sup>private</sup> |
| Document Subtype | subtype | subtype |
| Document Type | documentType | documentType |
| Exhibit Location | exhibitLocation | exhibitLocation |
| First Name | firstName | firstName |
| Government Agency | govAgency | govAgency |
| Government Agency Type | govAgencyType | govAgencyType |
| Is Withdrawn? | withdrawn | withdrawn |
| Last Name | lastName | lastName |
| Legacy ID | legacyId | legacyId |
| Organization Name | organization | organization |
| Page Count | pageCount | pageCount |
| Posted Date | postedDate | postedDate |
| Postmark Date | postmarkDate | postmarkDate |
| Reason Withdrawn | reasonWithdrawn | reasonWithdrawn |
| Received Date | receiveDate | receiveDate |
| Representative's Address | submitterRepAddress | submitterRepAddress |
| Representative's City, State & Zip | submitterRepCityState | submitterRepCityState |
| Restrict Reason | restrictReason | restrictReason |
| Restrict Reason Type | restrictReasonType | restrictReasonType |
| State/Province | stateProvinceRegion | stateProvinceRegion |
| Submitter Representative | submitterRep | submitterRep |
| Title | title | title |
| Tracking Number | trackingNbr | trackingNbr |
| Zip/Postal Code | zip | zip |

<sup>private</sup> This means it will always show up as null
within the API response.

<sup>1</sup> Attachment files are mostly for Comments but exceptions exist.
Must include "include=attachments" parameter in API call.

<sup>2</sup> Attribute is nested in a different part of the JSON.
Path: included->attributes->fileFormats->fileUrl.

<sup>3</sup> Same as in 2.

<sup>4</sup> Content files are for Non-Comment Documents.

<sup>5</sup> Contains a list of objects containing URLs.
The .htm version and the original version are provided.
.htm is a pure textual representation of the
original pdf file.
On the other hand, The CSV bulk data only contains the
.htm version of the file.


### Fields Missing In Bulk Data (8)
| X | Documents API Field Name | Comments API Field Name |
| --- | --- | --- |
| | address1 | address1 <sup>private</sup> |
| | address2 | address2 <sup>private</sup> |
| | email | email <sup>private</sup> |
| | fax | fax <sup>private</sup> |
| | modifyDate<sup>1</sup> | modifyDate<sup>1</sup> |
| | objectId<sup>2</sup> | objectId<sup>2</sup> |
| | openForComment<sup>3</sup> | openForComment<sup>3</sup> |
| | phone | phone <sup>private</sup> |

<sup>private</sup> This means it will always show up as null
within the API response.

<sup>1</sup> Will always change. Not valuable.

<sup>2</sup> Internal system id. Not valuable.

<sup>3</sup> Will always change. Not valuable.


### Fields Missing In Documents API (2)
| CSV Field Name | X | Comments API Field Name |
| --- | --- | --- |
| Comment on Document ID | | commentOnDocumentId |
| Duplicate Comments | | duplicateComments |


### Fields Missing In Comments API (20)
| CSV Field Name | Documents API Field Name | X |
| --- | --- | --- |
| Allow Late Comments | allowLateComments | |
| Author Date | authorDate | |
| Authors | authors | |
| CFR | cfrPart | |
| Comment Start Date | commentStartDate | |
| Comment Due Date | commentEndDate | |
| Effective Date | effectiveDate | |
| Exhibit Type | exhibitType | |
| Federal Register Number | frDocNum | |
| Implementation Date | implementationDate | |
| Media | media | |
| OMB/PRA Approval Number | ombApproval | |
| Page Length | paperLength | |
| Paper Width | paperWidth | |
| Related RIN(s) | additionalRins | |
| Source Citation | sourceCitation | |
| Special Instructions | regWriterInstruction | |
| Start End Page | startEndPage | |
| Subject | subject | |
| Topics | topics | |


### Fields Only In CSV Bulk Data (1)
| CSV Field Name | X | X |
| --- | --- | --- |
| FR Citation<sup>1</sup> | | |

<sup>1</sup> ID of Federal Regulation.


### Fields Only In Documents API (1)
| X | Documents API Field Name | X |
| --- | --- | --- |
| | frVolNum<sup>1</sup> | |

<sup>1</sup> ?


### Fields Only In Comments API (1)
| X | X | Comments API Field Name |
| --- | --- | --- |
| | | commentOn <sup>1</sup> |

<sup>1</sup> The objectId of the document
 the comment is attached to. Not valuable.


### Bulk Data Fields (60) (Ordered as they are provided)
| Field Name |
| --- |
| Document ID |
| Agency ID |
| Docket ID |
| Tracking Number |
| Document Type |
| Posted Date |
| Is Withdrawn? |
| Federal Register Number |
| FR Citation |
| Title |
| Comment Start Date |
| Comment Due Date |
| Allow Late Comments |
| Comment on Document ID |
| Effective Date |
| Implementation Date |
| Postmark Date |
| Received Date |
| Author Date |
| Related RIN(s) |
| Authors |
| CFR |
| Abstract |
| Legacy ID |
| Media |
| Document Subtype |
| Exhibit Location |
| Exhibit Type |
| Additional Field 1 |
| Additional Field 2 |
| Topics |
| Duplicate Comments |
| OMB/PRA Approval Number |
| Page Count |
| Page Length |
| Paper Width |
| Special Instructions |
| Source Citation |
| Start End Page |
| Subject |
| First Name |
| Last Name |
| City |
| State/Province |
| Zip/Postal Code |
| Country |
| Organization Name |
| Submitter Representative |
| Representative's Address |
| Representative's City, State & Zip |
| Government Agency |
| Government Agency Type |
| Comment |
| Category |
| Restrict Reason Type |
| Restrict Reason |
| Reason Withdrawn |
| Content Files |
| Attachment Files |
| Display Properties (Name, Label, Tooltip) |

### Documents API (65)
| Field Name |
| --- |
| additionalRins |
| address1 |
| address2 |
| agencyId |
| allowLateComments |
| authorDate |
| authors |
| category |
| cfrPart |
| city |
| comment |
| commentEndDate |
| commentStartDate |
| country |
| displayProperties |
| docAbstract |
| docketId |
| documentType |
| effectiveDate |
| email |
| exhibitLocation |
| exhibitType |
| fax |
| field1 |
| field2 |
| fileFormats |
| firstName |
| frDocNum |
| frVolNum |
| govAgency |
| govAgencyType |
| implementationDate |
| lastName |
| legacyId |
| media |
| modifyDate |
| objectId |
| ombApproval |
| openForComment |
| organization |
| originalDocumentId |
| pageCount |
| paperLength |
| paperWidth |
| phone |
| postedDate |
| postmarkDate |
| reasonWithdrawn |
| receiveDate |
| regWriterInstruction |
| restrictReason |
| restrictReasonType |
| sourceCitation |
| startEndPage |
| stateProvinceRegion |
| subject |
| submitterRep |
| submitterRepAddress |
| submitterRepCityState |
| subtype |
| title |
| topics |
| trackingNbr |
| withdrawn |
| zip |

### Comments API (46)
| Field Name |
| --- |
| address1 |
| address2 |
| agencyId |
| category |
| city |
| comment |
| commentOn |
| commentOnDocumentId |
| country |
| displayProperties |
| docAbstract |
| docketId |
| documentType |
| duplicateComments |
| email |
| fax |
| field1 |
| field2 |
| fileFormats |
| firstName |
| govAgency |
| govAgencyType |
| lastName |
| legacyId |
| modifyDate |
| objectId |
| openForComment |
| organization |
| originalDocumentId |
| pageCount |
| phone |
| postedDate |
| postmarkDate |
| reasonWithdrawn |
| receiveDate |
| restrictReason |
| restrictReasonType |
| stateProvinceRegion |
| submitterRep |
| submitterRepAddress |
| submitterRepCityState |
| subtype |
| title |
| trackingNbr |
| withdrawn |
| zip |
