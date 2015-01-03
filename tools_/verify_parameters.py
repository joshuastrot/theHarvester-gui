#Define the function to check the parameters in the GUI
def verify(domainName, dataSource, queryWithShodan, limitResults):
    if not domainName:
        return "Please enter a domain name."
    
    if not limitResults or str(limitResults).isdigit() == False:
        return "Please enter a valid number for your results limit."
    
    if dataSource == "Data Source":
        return "Please choose a data source."
    
    if domainName and limitResults and dataSource is not "Data Source":
        return True