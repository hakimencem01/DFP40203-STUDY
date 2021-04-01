print("Buy House Now");
print("Price : RM 300000");
houseprice = 300000;
aftercreditprice = 0;
percent = "";
creditstate = input("Are you have good credit ? [Y/N] ");
if(creditstate.lower()=="y"):
    aftercreditprice = houseprice + (houseprice*0.1);
    percent = "10%";

if(creditstate.lower()=="n"):
    aftercreditprice = houseprice + (houseprice*0.28);
    percent = "28";
print("You will entitled of "+percent+ " downpayment .\nFull housing price : RM "+str(aftercreditprice));
