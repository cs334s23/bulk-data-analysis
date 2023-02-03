
Results of Comparing Data between the CSV Bulk Download,
Documents API, and Comments API.

The data in the csv is organized completely flat in rows,
since that is the only form the CSV format offers.
Each row represents a document and has a unique document id
stored in the "Document ID" column.
Regarding the system as a whole, comments are considered as
documents and have their own document id.
This is how comments are stored in the csv, on separate
rows along with each document.

The documents api and the comments api together provide
the fields that are contained in the bulk csv data. Every comment
can be requested from the documents api as well since every comment
is a document. This means the documents api is sufficient but the
comments api can be used to find additional information about a comment.

Format of the JSON
{
	"data": {
		"id": "CMS-2022-0113-1871",
		"type": "documents" or "comments",
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
}

There are fields that are
common to all sources but every source has at least one field
not contained in the other sources. Listed below are the different
field combinations organized in triplets by their names
in the csv files, documents api
call, and comments api call, respectively.

TOTAL NUMBER OF FIELDS: 72


Only In CSV
	- FR Citation (useful, id of federal regulation)

Only in APIs
	- Both
		> objectId (internal system value, necessary?)
		> openForComment (boolean, necessary?)
		> modifyDate (date, necessary?)
		> many private attributes (always null so no point)
	- Only in Documents
		> frVolNum (necessary?)
	- Only in Comments
		> commentOn
			* not included in API docs
			* points to the objectId of the document the comment is attached to
			* similar to 


Common Fields (36)
========================================
(Abstract, docAbstract, docAbstract)
(Additional Field 1, field1, field1)
(Additional Field 2, field2, field2)
(Agency ID, agencyId, agencyId)
(Category, category, category)
(City, city, city)
(Comment, comment, comment)
(Country, country, country)
(Display Properties (Name, Label, Tooltip), displayProperties, displayProperties)
(Docket ID, docketId, docketId)
(Document Subtype, subtype, subtype)
(Document Type, documentType, documentType)
(Exhibit Location, exhibitLocation, exhibitLocation)
(First Name, firstName, firstName)
(Government Agency, govAgency, govAgency)
(Government Agency Type, govAgencyType, govAgencyType)
(Is Withdrawn?, withdrawn, withdrawn)
(Last Name, lastName, lastName)
(Legacy ID, legacyId, legacyId)
(Organization Name, organization, organization)
(Page Count, pageCount, pageCount)
(Posted Date, postedDate, postedDate)
(Postmark Date, postmarkDate, postmarkDate)
(Reason Withdrawn, reasonWithdrawn, reasonWithdrawn)
(Received Date, receiveDate, receiveDate)
(Representative's Address, submitterRepAddress, submitterRepAddress)
(Representative's City, State & Zip, submitterRepCityState, submitterRepCityState)
(Restrict Reason, restrictReason, restrictReason)
(Restrict Reason Type, restrictReasonType, restrictReasonType)
(State/Province, stateProvinceRegion, stateProvinceRegion)
(Submitter Representative, submitterRep, submitterRep)
(Title, title, title)
(Tracking Number, trackingNbr, trackingNbr)
(Zip/Postal Code, zip, zip)

(Attachment Files, included->attributes->fileFormats->fileUrl, SAME)
Attachment files are mostly for Non-Public Submisions but exceptions exist.
Must include "include=attachments" parameter in API call.

(Content Files, fileFormats, fileFormats)
Content files are only for Non-Public Submissions.


In APIs, but Not In Bulk Data (8)
========================================
(\_, address1, address1 (\*NOT PUBLIC\*))
(\_, address2, address2 (\*NOT PUBLIC\*))
(\_, email, email (\*NOT PUBLIC\*))
(\_, fax, fax (\*NOT PUBLIC\*))
(\_, modifyDate, modifyDate)
(\_, objectId, objectId)
(\_, openForComment, openForComment)
(\_, phone, phone (\*NOT PUBLIC\*))


Missing Only In Documents API (2)
========================================
(Comment on Document ID, \_, commentOnDocumentId)
(Duplicate Comments, \_, duplicateComments)


Missing Only In Comments API (19)
========================================
(Allow Late Comments, allowLateComments, \_)
(Author Date, authorDate, \_)
(Authors, authors, \_)
(CFR, cfrPart, \_)
(Comment Start Date, commentStartDate, \_)
(Comment Due Date, commentEndDate, \_)
(Effective Date, effectiveDate, \_)
(Exhibit Type, exhibitType, \_)
(Federal Register Number, frDocNum, \_)
(Implementation Date, implementationDate, \_)
(Media, media, \_)
(OMB/PRA Approval Number, ombApproval, \_)
(Page Length, paperLength, \_)
(Paper Width, paperWidth, \_)
(Related RIN(s) (Empty), ?additionalRins?, \_)
(Source Citation, sourceCitation, \_)
(Special Instructions, regWriterInstruction, \_)
(Start End Page, startEndPage, \_)
(Subject, subject, \_)
(Topics, topics, \_)
(Document ID, originalDocumentId, originalDocumentId (\*NOT PUBLIC\*))


Only In CSV Bulk Data (1)
========================================
(FR Citation, \_, \_)


Only In Documents API (1)
========================================
(\_, frVolNum, \_)


Only In Comments API (1)
========================================
(\_, \_, commentOn) Maybe In Microseconds?


Bulk Data (60)
====================
Document ID
Agency ID
Docket ID
Tracking Number
Document Type
Posted Date
Is Withdrawn?
Federal Register Number
FR Citation
Title
Comment Start Date
Comment Due Date
Allow Late Comments
Comment on Document ID
Effective Date
Implementation Date
Postmark Date
Received Date
Author Date
Related RIN(s)
Authors
CFR
Abstract
Legacy ID
Media
Document Subtype
Exhibit Location
Exhibit Type
Additional Field 1
Additional Field 2
Topics
Duplicate Comments
OMB/PRA Approval Number
Page Count
Page Length
Paper Width
Special Instructions
Source Citation
Start End Page
Subject
First Name
Last Name
City
State/Province
Zip/Postal Code
Country
Organization Name
Submitter Representative
Representative's Address
Representative's City, State & Zip
Government Agency
Government Agency Type
Comment
Category
Restrict Reason Type
Restrict Reason
Reason Withdrawn
Content Files
Attachment Files
Display Properties (Name, Label, Tooltip)


Documents API (65)
====================
additionalRins
allowLateComments
authorDate
authors
cfrPart
commentEndDate
commentStartDate
effectiveDate
exhibitLocation
exhibitType
frDocNum
frVolNum
implementationDate
media
ombApproval
paperLength
paperWidth
regWriterInstruction
sourceCitation
startEndPage
subject
topics
address1
address2
agencyId
city
category
comment
country
displayProperties
docAbstract
docketId
documentType
email
fax
field1
field2
fileFormats
firstName
govAgency
govAgencyType
objectId
lastName
legacyId
modifyDate
organization
originalDocumentId
pageCount
phone
postedDate
postmarkDate
reasonWithdrawn
receiveDate
restrictReason
restrictReasonType
stateProvinceRegion
submitterRep
submitterRepAddress
submitterRepCityState
subtype
title
trackingNbr
withdrawn
zip
openForComment


Comments API (46)
====================
commentOn
commentOnDocumentId
duplicateComments
address1
address2
agencyId
city
category
comment
country
displayProperties
docAbstract
docketId
documentType
email
fax
field1
field2
fileFormats
firstName
govAgency
govAgencyType
objectId
lastName
legacyId
modifyDate
organization
originalDocumentId
pageCount
phone
postedDate
postmarkDate
reasonWithdrawn
receiveDate
restrictReason
restrictReasonType
stateProvinceRegion
submitterRep
submitterRepAddress
submitterRepCityState
subtype
title
trackingNbr
withdrawn
zip
openForComment
