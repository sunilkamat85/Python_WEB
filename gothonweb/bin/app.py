
import web

urls = (
  '/hello', 'some'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")
class some:
    def GET(self):
#        sun = "TRAINING / LEARNING WEBSITE"
#	form = web.input(name="nobody", wat=None)
#	if form.wat:
#		sun = "%s %s" % (form.name, form.wat)
#	        return render.foo(sun = sun)
#	else:
#		return "Error: wat is required"
	return render.hello_form()
    def POST(self):
	form = web.input()
	greeting = "%s, %s" % (form.greet, form.name)
	return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
