class Page(object):
    bbs_url = 'https://mail.126.com'
    def __init__(self,selenium_driver,base_url=bbs_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert  self.on_page(),'did not land on %s' %url

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self,scr):
        return self.driver.execute_script(scr)