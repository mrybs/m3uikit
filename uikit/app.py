from slinn import Dispatcher, LinkFilter, HttpResponse
from ntml.ntmlc import ntml_compile

meals = {
	'br': {'tag': 'br'},
	'Button': {'tag': 'button', 'props':({'style': """
		background: #C2E7FF;
		color: #000000;
		padding: 20px;
		border-radius: 20px;
		border: 0;
		font-size: 16px;
		text-align: center;
		"""}, [])},
	'CButton': {'tag': 'button', 'props':({'style': """
		background: #C2E7FF;
		color: #000000;
		padding: auto;
		border-radius: 40px;
		border: 0;
		font-size: 24px;
		font-weight: bold;
		width: 64px;
		height: 64px;
		margin: 3px;
		text-align: center;
		"""}, [])},
	'MButton': {'tag': 'button', 'props':({'style': """
		background: #00000000;
		color: #000000;
		padding: auto;
		border-radius: 40px;
		border: 0;
		font-size: 20px;
		font-weight: bold;
		width: 55px;
		height: 35px;
		margin: 3px;
		text-align: center;
		"""}, [])},
	'SButton': {'tag': 'button', 'props':({'style': """
		background: #C2E7FF;
		color: #000000;
		padding: auto;
		border-radius: 40px;
		border: 0;
		font-size: 14px;
		font-weight: bold;
		width: 26px;
		height: 26px;
		margin: 3px;
		text-align: center;
		"""}, [])},
	'LInput': {'tag': 'input', 'props': ({'style': """
		background: #C2E7FF;
		color: #000000;
		width: calc(100% - 1px);
		height: 125px;
		border: 0;
		margin: 0;
		padding: 0;
		outline: 0;
		text-align: right;
		font-size: 48px;
		border-bottom-left-radius: 20px;
		border-bottom-right-radius: 20px;
		"""}, [])},
	'ThreeDots': {'tag': 'button', 'props': ({'style':"""
		content: '︙';
		"""}, [])}
}
 
dp = Dispatcher()

# Write your code down here   
@dp(LinkFilter('styles.css'))
def styles(request):
	return render('styles.css')

@dp(LinkFilter(''))
def index(request):
	return render('index.ntml')



def render(path):
	try:
		extension = path.split('.')[-1]
		match extension:
			case 'html':
				with open(path, 'r') as f:
					return HttpResponse(f.read(), content_type='text/html')
			case 'ntml':
				with open(path, 'r') as f:
					return HttpResponse(ntml_compile(f.read(), path, meals), content_type='text/html')
			case 'css':
				with open(path, 'r') as f:
					return HttpResponse(f.read(), content_type='text/css')
	except FileNotFoundError:
		return '404 Not Found'
