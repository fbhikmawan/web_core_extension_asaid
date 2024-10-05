/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

patch(WebClient.prototype, {
    setup() {
        super.setup();

        const titleService = useService("title");
        let companyName = "Odoo";
        if (session.user_companies && session.user_companies.allowed_companies) {
            const currentCompanyId = session.user_companies.current_company;
            const company = session.user_companies.allowed_companies[currentCompanyId];
            if (company) {
                companyName = company.name;
            }
        }

        // Set the title parts to include the company name
        titleService.setParts({ zopenerp: companyName });
    },
});