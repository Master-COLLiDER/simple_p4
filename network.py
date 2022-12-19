from p4utils.mininetlib.network_API import NetworkAPI

class Network(NetworkAPI):

    def __init__(self):
        super(Network, self).__init__()


    # build a treT(depth=2, fanout=3, enable_all=True)
    def build( self, depth=1, fanout=3 ):
        self.hostNum = 1
        self.switchNum = 1
        self.addP4Switch('s1',cli_input='s1-commands.txt')
        self.addHost('h1')
        self.addHost('h2')
        self.addHost('h3')
        self.addLink('s1','h1')
        self.addLink('s1','h2')
        self.addLink('s1','h3')

    def start(self):
        self.setLogLevel('info')
        self.enableCli()
        self.setP4SourceAll('simple_program.p4')


        # Nodes general options
        # self.enablePcapDumpAll()
        # self.enableLogAll(

        # Assignment strategy
        self.mixed()

        # Start network
        self.startNetwork()

Network().start()
 