import { api } from '@/plugins/axios'

export default {
    //async getAllItems(): Promise<Item[]> {
    //const response = await axios.get<Item[]>(`${API_BASE_URL}/items`);
    //return response.data;
    //},
    async getItemAll(url:string) {
        try { const response = await api.get(url);
            //console.log('Api getItemAll: ', response.data)
            return response.data;
        }
        catch (error) { return error; }
    },

    async getItemId(url:string, id:number) {
        try { const response = await api.get(`${url}/${id}`);
            return response.data;
        }
        catch (error) { return error; }
    },

    async addItem(url:string, data:any) {
        //console.log('Api addItem: ', url)
        try { const response = await api.post(url, data);
            return response.data;
        }
        catch (error) { return error; }
    },

    async updItem(url:string, id:number, data:any) {
        try { const response = await api.put(`${url}/${id}`, data);
            return response.data;
        }
        catch (error) { return error; }
    },
    
    async delItem(url:string, id:number) {
        try { const response = await api.delete(`${url}/${id}`);
            return response.data;
        }
        catch (error) { return error; }
    }
};