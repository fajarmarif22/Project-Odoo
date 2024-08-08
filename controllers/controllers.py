# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64
import json
import requests
import csv
import io

class TrainingController(http.Controller):
    @http.route('/download/data', type='http', auth='public', methods=['GET'], csrf=False)
    def download_data(self, **kwargs):
        records = request.env['training.course'].search([])
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Name', 'Description'])
        for record in records:
            writer.writerow([record.name, record.description])
        
        output.seek(0)
        data = output.read()
        output.close()
        
        return request.make_response(
            data,
            headers=[
                ('Content-Type', 'text/csv'), 
                ('Content-Disposition', 'attachment;filename="data_training_course.csv"')
            ]
        )
    
    @http.route('/api/training/course/list', type='http', auth='public', methods=['GET'], csrf=False)
    def training_course_list(self, **kw):
        try:
            courses = request.env['training.course'].search([])
        except:
            return http.Response("<h3>Can't Access Training Course List</h3>", status=500)
        
        json_data = []
        for course in courses:
            json_record = {
                'name': course.name,
                'description': course.description
            }
            json_data.append(json_record)
        
        return http.Response(json.dumps(json_data), headers={'Content-Type': 'application/json'})

    @http.route('/api/training/course/create', type='http', auth='public', methods=['POST'], csrf=False)
    def training_course_create(self, **kw):
        try:
            data = json.loads(request.httprequest.data)
            
            name = data.get('name')
            description = data.get('description')
            
            if not name:
                return http.Response(json.dumps({'error': 'Name is required'}), status=400, headers={'Content-Type': 'application/json'})
            
            Record = request.env['training.course']
            new_record = Record.create({
                'name': name,
                'description': description,
            })
            
            return http.Response(json.dumps({'message': 'Success Create', 'id': new_record.id}), status=201, headers={'Content-Type': 'application/json'})
        except Exception as e:
            return http.Response(json.dumps({'error': str(e)}), status=500, headers={'Content-Type': 'application/json'})


    @http.route('/api/training/course/update', type='http', auth='public', methods=['POST'], csrf=False)
    def training_course_update(self, **kw):
        try:
            data = json.loads(request.httprequest.data)

            id = data.get('id')
            name = data.get('name')
            description = data.get('description')
            
            if not id:
                return http.Response(json.dumps({'error': 'ID is required'}), status=400, headers={'Content-Type': 'application/json'})

            Record = request.env['training.course'].search([('id', '=', id)], limit=1)
            if Record:
                Record.write({
                    'name': name,
                    'description': description,
                })
                return http.Response(json.dumps({'message': 'Success Update'}), status=200, headers={'Content-Type': 'application/json'})
            else:
                return http.Response(json.dumps({'error': 'Record not found'}), status=404, headers={'Content-Type': 'application/json'})
        except Exception as e:
            return http.Response(json.dumps({'error': str(e)}), status=500, headers={'Content-Type': 'application/json'})

    @http.route('/api/training/course/delete', type='http', auth='public', methods=['POST'], csrf=False)
    def training_course_delete(self, **kw):
        try:
            data = json.loads(request.httprequest.data)

            id = data.get('id')
            
            if not id:
                return http.Response(json.dumps({'error': 'ID is required'}), status=400, headers={'Content-Type': 'application/json'})

            Record = request.env['training.course'].search([('id', '=', id)], limit=1)
            if Record:
                Record.unlink()
                return http.Response(json.dumps({'message': 'Success Delete'}), status=200, headers={'Content-Type': 'application/json'})
            else:
                return http.Response(json.dumps({'error': 'Record not found'}), status=404, headers={'Content-Type': 'application/json'})
        except Exception as e:
            return http.Response(json.dumps({'error': str(e)}), status=500, headers={'Content-Type': 'application/json'})

# class OdooTraining(http.Controller):
#     @http.route('/odoo_training/odoo_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_training/odoo_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_training.listing', {
#             'root': '/odoo_training/odoo_training',
#             'objects': http.request.env['odoo_training.odoo_training'].search([]),
#         })

#     @http.route('/odoo_training/odoo_training/objects/<model("odoo_training.odoo_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_training.object', {
#             'object': obj
#         })

