import requests
from lxml import etree
from variables import market_list as market_list,lod_base_url as lod_base_url,shoplocal_base_url as shoplocal_base_url,lod_list1 as lod_list1,shoplocal_list1 as shoplocal_list1



def cleanup(content):
    if content.endswith("\n"):
        return content[:-1]
    else:
        return content

def parse_api_in_xml(listToBuild, baseURL, marketField):

    CONTENT = requests.get(baseURL+marketField).content
    root = etree.fromstring(CONTENT)
    for (vehicle,offerRegion,offerMarket,type1,offerType,offerAmount,offerAmountQualifier,
         offerTermPreQualifier,offerTerm,offerTermPostQualifier,downPayment,downPaymentQualifier,
         offerDescriptionShort,offerDescriptionLong,modelDescription1,modelDescription2,offerDisclaimer,
         offerDefault,modelDescription3,modelYear,otherOffers,additionalOffer,offerCategory) in zip(root.xpath("//vehicle"),root.xpath("//offerRegion"),
                                                                                                    root.xpath("//offerMarket"),root.xpath("//type"),
                                                                                                    root.xpath("//offerType"),root.xpath("//offerAmount"),
                                                                                                    root.xpath("//offerAmountQualifier"),root.xpath("//offerTermPreQualifier"),
                                                                                                    root.xpath("//offerTerm"),root.xpath("//offerTermPostQualifier"),
                                                                                                    root.xpath("//downPayment"),root.xpath("//downPaymentQualifier"),
                                                                                                    root.xpath("//offerDescriptionShort"),root.xpath("//offerDescriptionLong"),
                                                                                                    root.xpath("//modelDescription1"), root.xpath("//modelDescription2"),
                                                                                                    root.xpath("//offerDisclaimer"),root.xpath("//offerDefault"),
                                                                                                    root.xpath("//modelDescription3"),root.xpath("//modelYear"),
                                                                                                    root.xpath("//otherOffers"),root.xpath("//additionalOffer"),
                                                                                                    root.xpath("//offerCategory")):
       
       
        listToBuild.append([
                        (offerRegion.text),
                        (offerMarket.text),
                        (vehicle.attrib.get("model")),
                        (vehicle.attrib.get("modelDisplayName")),
                        (type1.text),
                        (offerType.text),
                        (offerAmount.text),
                        (offerAmountQualifier.text),
                        (offerTermPreQualifier.text),
                        (offerTerm.text),
                        (offerTermPostQualifier.text),
                        (downPayment.text),
                        (downPaymentQualifier.text),
                        (offerDescriptionShort.text),
                        (offerDescriptionLong.text),
                        (modelDescription1.text),
                        (modelDescription2.text),
                        cleanup((offerDisclaimer.text)),
                        (offerDefault.text),
                        (modelDescription3.text),
                        (modelYear.text),
                        (otherOffers.text),
                        (additionalOffer.text),
                        (offerCategory.text)  
                        ])
    #print '\n\n\n' + "BUILT LIST: "
    #print listToBuild
    #ileOut.write('\n' + num)
    #fileOut.write('\n\n\n' + "BUILT LIST: ")
    #fileOut.write('\n' + listToBuild)
    

def compare_lists(feed1,feed2):

        try:
            for item in feed1:

                if item in feed2:
                    #print "PASS:"
                    #print item
                    continue
                else:
                    print "***************ERROR FOUND***************"
                    print "item in feed 1 that doesn't match:"
                    print item
                    continue
                  
            for item in feed2:
                if item not in feed1:
                    print "***************ERROR FOUND***************"
                    print "item in feed 2 that doesn't match:"
                    print item
                    continue
                
        except IndexError:
            print "\n \nIndexError received."

        feed1 = []
        feed2 = []
  


for market in market_list:
    print "Market under test: " + str(market)
    parse_api_in_xml(list1, list1_base_url, market)
    parse_api_in_xml(list2, list2_base_url, market)
    compare_lists(list1,list2)
    #print list1
    #print list2

