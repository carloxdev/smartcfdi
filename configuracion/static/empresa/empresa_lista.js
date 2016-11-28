
var card_filtros = null
var card_resultados = null
var url = window.location
var url_consulta = ""
var url_editar = ""

if (url.pathname.search("smart") > 0) {
    url_consulta = url.origin + "/smart/api/empresas/"
    url_editar = url.origin + "/smart/empresas/editar/"
}
else {
    url_consulta = url.origin + "/api/empresas/"
    url_editar = url.origin + "/empresas/editar/"
}


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_resultados = new TargetaResultados()

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)
})

$(window).resize(function() {
    card_resultados.kGrid.data("kendoGrid").resize()
})

/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.$divGrid = $('#resultados')
    this.kFields = null
    this.kFuenteDatos = null
    this.kRows = null
    this.kColumns = null
    this.kToolbar = null
    this.kGrid = null

    this.init()
}
TargetaResultados.prototype.init = function () {

    kendo.culture("es-MX")
    
    this.kFields = {
        clave: { editable: false, type: "string" },
        razon_social: { editable: false, type: "string" },
        logo: { editable: false, type: "string" },
        rfc: { editable: false, type: "string" },
        ciec: { editable: false, type: "string" },
        activa: { editable: false, type: "string" },
        usuario: { editable: false, type: "string" },
        email: { editable: false, type: "string" },
        created_date: { editable: false, type: "string" },
        updated_date: { editable: false, type: "string" },
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        serverPaging: true,
        pageSize: 20,
        transport: {
            read: {

                url: url_consulta,
                type: "GET",
                dataType: "json",
            },
            // parameterMap: function (data, action) {
            //     if (action === "read") {

            //         return {
            //             page: data.page,
            //             pageSize: data.pageSize,
            //             empresa__clave: card_filtros.$empresa.val(),
            //             fecha_min: card_filtros.$fecha_inicio.val(),
            //             fecha_max: card_filtros.$fecha_fin.val(),
            //             emisor_rfc: card_filtros.$emisor_rfc.val(),
            //             emisor_nombre: card_filtros.$emisor_nombre.val(),
            //             uuid: card_filtros.$uuid.val(),
            //             estadoSat: card_filtros.$estado_sat.val(),
            //             folio: card_filtros.$folio.val(),
            //             serie: card_filtros.$serie.val(),
            //             fechaTimbrado_min: card_filtros.$fecha_timbrado_inicio.val(),
            //             fechaTimbrado_max: card_filtros.$fecha_timbrado_fin.val(),
            //             comprobacion: card_filtros.$comprobacion.val(),
            //         }
            //     }
            // }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                id: "uuid",    
                fields: this.kFields    
            }
        },
        error: function (e) {
			alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    })

    this.kToolbar = [
        {
            name: "copyRows",
            text: "Copy Rows",
            click: function (e) {
                alert('test');
            }
        },
    ]

    this.kColumns = [
        { field: "clave", title: "Clave", width: "100px" },
        { field: "razon_social", title: "Razon Social", width: "200px" },
        // { field: "logo", title: "logo", width: "200px" },
        { field: "rfc", title: "RFC", width: "150px" },
        { field: "ciec", title: "CIEC", width: "150px" },
        { 
            field: "activa", 
            title: "Estado", 
            width: "80px",
            template: "#= activa ? 'Activa' : 'Inactiva' #"
        },
        { field: "usuario", title: "Usuario", width: "150px" },
        { field: "email", title: "Email", width: "150px" },
        { 
            field: "created_date", 
            title: "Creado por", 
            width: "100px",
            template: "#= kendo.toString(kendo.parseDate(created_date, 'yyyy-MM-dd'), 'dd-MM-yyyy') #",
        },
        { 
            field: "updated_date", 
            title: "Actualizado por", 
            width: "110px",
            template: "#= kendo.toString(kendo.parseDate(updated_date, 'yyyy-MM-dd'), 'dd-MM-yyyy') #",

        },
        {
           command: {
               text: "Editar",
               click: this.editar_Registro,
           },
           title: " ",
           width: "110px"
        },
    ]

    this.kGrid = this.$divGrid.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        resizable: true,
        editable: true,
        pageable: true,
        selectable: true,
        scrollable: true,
        columns: this.kColumns,
    })

}
TargetaResultados.prototype.buscar = function (e) {
    this.kFuenteDatos.page(1)
}
TargetaResultados.prototype.editar_Registro = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk;
}