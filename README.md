# PIZZA
## Step 1:
 Move to Current Downloaded Location using cmd or terminal, if you see the project in your current directory 

## Step 2:
If you want install in seperate location using virtaulenv or else continue step 3<br>
> In windows,<br>
`pip install virtualenvwrapper-win` <br>
> Once Completed, create virtual environment using <br>
`mkvirtualenv env_name `<br>
> If want Use it again use, <br>
`workon env_name `<br>

## Step 3:
Install package using ` pip install -r requirements.txt `
  
## setp 4:
Create migration files `python manage.py makemigrations`
  
## setp 5:
 Updation in database in mongoDB  `python manage.py migrate`

## Step 6:
Create superuser for create pizza and toppings `python manage.py createsuperuser`


## Step 7:
Run django server  `python manage.py runserver`



### **Documentations for endpoint **

### 1. Create Topping:
##### &emsp;&emsp;METHOD: POST
##### &emsp;&emsp;HEADERS: 
##### &emsp;&emsp;&emsp;&emsp;Authorization: Token abcdefghijklmnopqrstuvwxyz
##### &emsp;&emsp;URL: 
##### &emsp;&emsp;&emsp;&emsp;/api/topping/add/
##### &emsp;&emsp;REQUEST:
```
	"name": string,
	"addPrice": float
 ```
##### &emsp;&emsp;RESPONSE:
```
	"success": boolean,
	"errors": dict,
	"data": dict,
```

##### &emsp;&emsp;EXAMPLES:
##### &emsp;&emsp; &emsp;&emsp;CASE 1:  Validation errors
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         {}
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 400
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 {  
			 "success":  false,  
			 "data":  null,  
			 "errors":  { 
				 "name":  [  "This field is required."  ], 
				 "addPrice":  [  "This field is required."  ]  
			}  
		}
```
##### &emsp;&emsp; &emsp;&emsp;CASE 2:  header not set
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
       any
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 401
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		no response
```

##### &emsp;&emsp; &emsp;&emsp;CASE 3:  Created successfully
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
        {
            "name":"Onion",
            "addPrice":23
        }
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 201
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		{
		    "success": true,
		    "errors": null,
			"data":{
				"_id":"6120b31f91b713cc357aca85",
				"id" : 1, 
				"name" : "Onion", 
				"addPrice" : 23
			}
		}
```



### 2. All Toppings:
##### &emsp;&emsp;METHOD: GET
##### &emsp;&emsp;URL: 
##### &emsp;&emsp;&emsp;&emsp;/api/topping/
##### &emsp;&emsp;REQUEST:
```
	page:int (optional)default page1 with limit of 10
 ```
 ##### &emsp;&emsp;RESPONSE:
```
	"success": boolean,
	"errors": dict,
	"data": dict,
```
##### &emsp;&emsp;EXAMPLES:
```
{  
	"success":  true,  
	"data":  [{  
		"id":  8,  
		"name":  "Onion",  
		"addPrice":  23.0 
	}], 
	"errors":  null  
}

```

### 3. Create Pizza:
##### &emsp;&emsp;METHOD: POST
##### &emsp;&emsp;HEADERS: 
##### &emsp;&emsp;&emsp;&emsp;Authorization: Token abcdefghijklmnopqrstuvwxyz
##### &emsp;&emsp;URL: 
##### &emsp;&emsp;&emsp;&emsp;/api/pizza/add/
##### &emsp;&emsp;REQUEST:
```
	"type":list of dict
		"name":string,
		"addPrice":float,
	"size":list of dict 
		"size":string, 
		"addPrice":float,
	"name":string,
	"price":float
	"defaultTopping":list of topping primary key,
 ```
##### &emsp;&emsp;RESPONSE:
```
	"success": boolean,
	"errors": dict,
	"data": dict,
```

##### &emsp;&emsp;EXAMPLES:
##### &emsp;&emsp; &emsp;&emsp;CASE 1:  Validation errors
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         {}
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 400
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 { 
			 "success":  false,  
			 "data":  null,  
			 "errors":  {  
				 "type":  [  "This field is required."  ],
				 "size":  [  "This field is required."  ],
				 "defaultTopping":  [  "This field is required."  ],  
				 "name":  [  "This field is required."  ],  
				 "price":  [  "This field is required."  ] 
			 }  
		}
```
##### &emsp;&emsp; &emsp;&emsp;CASE 2:  header not set
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
       any
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 401
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		no response
```

##### &emsp;&emsp; &emsp;&emsp;CASE 3:  Created successfully
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
{
	"type":[
		{"name":"Regular","addPrice":0}, 
		{"name":"Square","addPrice":20}
	],
	"size":[
		{"size":"Small", "addPrice":0}, 
		{"size":"Medium", "addPrice":35}, 
		{"size":"Large", "addPrice":70}
	],
	"name":"cheesy",
	"price":120,
	"defaultTopping":[1, 2]
}
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 201
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		{
		    "success": true,
		    "errors": null,
			"data":object of pizza,
		}
```


### 4. Edit Pizza:
##### &emsp;&emsp;METHOD: POST
##### &emsp;&emsp;URL: 
##### &emsp;&emsp;&emsp;&emsp;/api/pizza/str:id/ 
##### &emsp;&emsp;REQUEST:
```
	"type":list of dict
		"name":string,
		"addPrice":float,
	"size":list of dict 
		"size":string, 
		"addPrice":float,
	"name":string,
	"price":float
	"defaultTopping":list of topping primary key,
 ```
##### &emsp;&emsp;RESPONSE:
```
	"success": boolean,
	"errors": dict,
	"data": dict,
```

##### &emsp;&emsp;EXAMPLES:
##### &emsp;&emsp; &emsp;&emsp;CASE 1:  url id not found
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         any
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 404
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 {  
			 "success":  false,  
			 "data":  null,  
			 "errors":  "Bad request"  
		}
```
##### &emsp;&emsp; &emsp;&emsp;CASE 2:  Validation errors
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         {}
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 400
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 { 
			 "success":  false,  
			 "data":  null,  
			 "errors":  {  
				 "type":  [  "This field is required."  ],
				 "size":  [  "This field is required."  ],
				 "defaultTopping":  [  "This field is required."  ],  
				 "name":  [  "This field is required."  ],  
				 "price":  [  "This field is required."  ] 
			 }  
		}
```

##### &emsp;&emsp; &emsp;&emsp;CASE 3:  update successfully
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
{
	"type":[
		{"name":"Regular","addPrice":0}, 
		{"name":"Square","addPrice":20}
	],
	"size":[
		{"size":"Small", "addPrice":0}, 
		{"size":"Medium", "addPrice":50}, 
		{"size":"Large", "addPrice":70}
	],
	"name":"cheesy",
	"price":120,
	"defaultTopping":[1, 2]
}
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 201
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		{
		    "success": true,
		    "errors": null,
			"data":updated object of pizza will be return,
		}
```



### 5. Delete Pizza:
##### &emsp;&emsp;METHOD: DELETE
##### &emsp;&emsp;URL: 
##### &emsp;&emsp;&emsp;&emsp;/api/pizza/str:id/ 
##### &emsp;&emsp;REQUEST:
```
None
```
##### &emsp;&emsp;RESPONSE:
```
	"success": boolean,
	"errors": dict,
	"data": dict,
```

##### &emsp;&emsp;EXAMPLES:
##### &emsp;&emsp; &emsp;&emsp;CASE 1:  url id not found
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         any
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 404
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 {  
			 "success":  false,  
			 "data":  null,  
			 "errors":  "Bad request"  
		}
```
##### &emsp;&emsp; &emsp;&emsp;CASE 2:  Validation errors
##### &emsp;&emsp; &emsp;&emsp;INPUT:
```
         None
```
##### &emsp;&emsp; &emsp;&emsp;OUTPUT:
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;STATUS: 202
##### &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;JSON RESULT:
```
		 {  
			 "success":  true,  
			 "data":  {  
				 "description":  "6120b4f4c5f587da3c99fdbe delete successfully"  
			  },  
			 "errors":  null  
		}
```
