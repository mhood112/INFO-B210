import csv

def get_shows_by_network(file_path):
    network = input("Enter a network from List below: \nAMC\nFOX\nNickelodeon\nBBC One\nCBS\nABC\nNBC\nThe CW\nHBO\nShowtime\nFX\nUSA Network\nTNT\nSyfy\nStarz\nNHK\nFuji TV\nDisney XD\nSyfy\nNTV\nAdult Swim\nITV1\nSyndication\nChannel 4\nFX\n \nCTV Sci-Fi Channel\nCinemax\nHistory\nNational Geographic\nTV Tokyo\nFox Kids\nUPN\nWOWOW\nComedy Central\nScience\nSVT1\nUSA Network\nFXX\nThe WB\nBBC Three\nInvestigation Discovery\nHallmark Channel\nCartoon Network\nNewsNation\nCBC\nDiscovery\nSky Showcase\nParamount Network\nW\nDR1\nCBBC\nZDF\nE4\nShowcase\nSundanceTV\nFood Network\nAudience Network\nNational Geographic Wild\nA&E\nMTV\nAntena 3\nSky Atlantic\nSUN-TV\nCNBC\nBBC Four\nNine Network\nFreeform\nTravel Channel\ntruTV\nNPO 3\nLifetime\nNRK1\nLa 1\nCTV\nRTÉ ONE\nDisney Channel\nEl Rey Network\nAnimal Planet\nPBS\nGlobal\nE!\nThe Movie Network\nNetwork 10\nTV Land\nHallmark Movies & Mysteries\nBET\nBBC America\nDave\nNagoya Broadcasting Network\nTokyo MX\nAT-X\nIFC\nCanal+\nChallenge\nS4C\nREELZ\nITV2\nVisionTV\nSBS\nCNN\nKBS2\nH2\nAnimax\nTV Kanagawa\nNicktoons\nTF1\nChannel 10\nMnet\nGulli\nMBS\nTV4\nBravo\nMagnolia Network\nSky Arts\nVRT 1\nMotorTrend\nMCOT HD\nSeven Network\nCMT\nYTV\nRTL\nTLC\nTV Asahi\nVH1\nMGM+\nTV Saitama\nFamily Channel\nPay-Per-View\nT+E\nFox News Channel\nSmithsonian Channel\nOxygen\nABC Entertains\nBS11\nFrance 4\nCitytv\nTVO\nG4\nCooking Channel\nNick Jr.\nnick@nite\nKanal 5\nChannel 5\nMTV2\nDiscovery Family\nBoomerang\nAXS TV\nUP TV\nCentric\nPop\nDestination America\nTelecinco\nCuatro\nTVE\nTeenNick\nRTP1\nSky Witness\nGAC Family\nNBCSN\nFrance 2\nRTL4\nLogo TV\nWE tv\nHBO Canada\nFYI\nNPO 1\nESPN\nSBS 6\nQuest\nDR3\nRTVE\nLa Sexta\nLondon Weekend Television\nVTM\nKids Station\nMBC\nOvation\nITVBe\nFox Reality Channel\nHGTV\nPivot\nHLN\nAHC\nMSNBC\nAl Jazeera America\nGolf Channel\nEsquire Network\nLifetime Movies\nOutdoor Channel\nGame Show Network\nBloomberg TV\nThe Weather Channel\nORF 1\nOprah Winfrey Network\nChannel 8\nПервый канал\nNPO 2\nTVB\nTV One\nGTH on Air\nFox Sports 1\nDiscovery Life\nBounce\nKBS\n").strip()
    shows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # Skip the header line
        next(reader)
        
        for row in reader:
            # Assuming the CSV format is: title,...,network (network is the 9th column)
            if len(row) < 9:
                continue
            title, show_network = row[0].strip(), row[8].strip()
            #print(f"Checking show: {title} on network: {show_network}")  # Debug print
            if show_network.lower() == network.lower():
                shows.append(title)
    
    if shows:
        print(f"Shows available on {network}:")
        for show in shows:
            print(show)
    else:
        print(f"No shows found for the network: {network}")

# Example usage
get_shows_by_network('Tv_Show.csv')
