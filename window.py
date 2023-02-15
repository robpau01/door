from flask import Flask, Response

app = Flask(__name__)
            
@app.route('/')
def window():
                xml = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
                    <window>    
                        <items>
                            <item id=\"234738947\">
                                <id>234738947</id>
                                <details>
                                    <material>Glas</material>
                                    <style>Toned</style>
                                    <size>15x65</size>
                                </details>
                            </item>
                            <item id=\"2344568947\">
                                <id>2344568947</id>
                                <details>
                                    <material>Plastic</material>
                                    <style>None</style>
                                    <size>15x65</size>
                                </details>
                            </item>
                            <item id=\"235435\">
                                <id>235435</id>
                                <details>
                                    <material>Plywood</material>
                                    <style>Blacked</style>
                                    <size>15x64</size>
                                </details>
                            </item>
                        </items>
                    <copyright>2002 - Martin</copyright>
                    </window>'''
return Response(xml, mimetype='xml')"
